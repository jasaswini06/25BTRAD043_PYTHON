/**
 * app.js — University Lost & Found Registry Engine
 * Handles live filtering, search keyboard shortcuts, modals, copy-to-clipboard,
 * animated stat counters, and toast notifications.
 */

(function () {
    // 1. Stats Counter Animation: requestAnimationFrame over 600ms, non-repeating
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const counters = document.querySelectorAll('.counter-stat');
    if (counters.length && !prefersReducedMotion) {
        const duration = 600;
        const startTime = performance.now();
        function updateCounters(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easeOutQuad = 1 - (1 - progress) * (1 - progress);

            counters.forEach(counter => {
                const target = parseInt(counter.getAttribute('data-target') || '0', 10);
                const currentVal = Math.round(easeOutQuad * target);
                counter.textContent = currentVal;
            });

            if (progress < 1) {
                requestAnimationFrame(updateCounters);
            } else {
                counters.forEach(c => c.textContent = c.getAttribute('data-target'));
            }
        }
        requestAnimationFrame(updateCounters);
    }

    // 2. Toast feedback helper
    window.showToast = function(message) {
        const toast = document.getElementById('toast');
        const msgEl = document.getElementById('toast-msg');
        if (!toast || !msgEl) return;
        msgEl.textContent = message;
        toast.classList.remove('translate-y-16', 'opacity-0', 'pointer-events-none');
        clearTimeout(window._toastTimeout);
        window._toastTimeout = setTimeout(() => {
            toast.classList.add('translate-y-16', 'opacity-0', 'pointer-events-none');
        }, 2600);
    };

    // 3. Search & Filter Engine (Index Page)
    const searchInput = document.getElementById('search-input');
    const clearSearchBtn = document.getElementById('clear-search-btn');
    const tableBody = document.getElementById('inventory-table-body');

    if (searchInput && tableBody) {
        const rows = Array.from(tableBody.querySelectorAll('.item-row'));
        const emptyState = document.getElementById('table-empty-state');
        const countBadge = document.getElementById('filtered-count-badge');
        const resetBtn = document.getElementById('reset-all-filters');
        const emptyResetBtn = document.getElementById('empty-reset-btn');

        let currentType = 'all';
        let currentStatus = 'all';
        let currentCat = 'all';

        function filterItems() {
            const query = (searchInput.value || '').trim().toLowerCase();
            let visibleCount = 0;

            if (query.length > 0) {
                clearSearchBtn.classList.remove('hidden');
            } else {
                clearSearchBtn.classList.add('hidden');
            }

            const isFiltered = (currentType !== 'all' || currentStatus !== 'all' || currentCat !== 'all' || query.length > 0);
            if (isFiltered && resetBtn) {
                resetBtn.classList.remove('hidden');
            } else if (resetBtn) {
                resetBtn.classList.add('hidden');
            }

            rows.forEach(row => {
                const type = (row.getAttribute('data-type') || '').toUpperCase();
                const status = (row.getAttribute('data-status') || '').toLowerCase();
                const cat = (row.getAttribute('data-cat') || '').toLowerCase();
                const ref = (row.getAttribute('data-ref') || '').toLowerCase();
                const title = (row.getAttribute('data-title') || '').toLowerCase();
                const location = (row.getAttribute('data-location') || '').toLowerCase();
                const name = (row.getAttribute('data-name') || '').toLowerCase();

                const matchType = (currentType === 'all' || type === currentType.toUpperCase());
                const matchStatus = (currentStatus === 'all' || status === currentStatus.toLowerCase());
                const matchCat = (currentCat === 'all' || cat === currentCat.toLowerCase());
                const matchQuery = !query || title.includes(query) || ref.includes(query) || location.includes(query) || name.includes(query);

                if (matchType && matchStatus && matchCat && matchQuery) {
                    row.classList.remove('hidden');
                    visibleCount++;
                } else {
                    row.classList.add('hidden');
                }
            });

            if (countBadge) {
                countBadge.textContent = `${visibleCount} ${visibleCount === 1 ? 'entry' : 'entries'}`;
            }

            if (emptyState) {
                if (visibleCount === 0) {
                    emptyState.classList.remove('hidden');
                } else {
                    emptyState.classList.add('hidden');
                }
            }
        }

        // Search Input Events
        searchInput.addEventListener('input', filterItems);

        if (clearSearchBtn) {
            clearSearchBtn.addEventListener('click', () => {
                searchInput.value = '';
                filterItems();
                searchInput.focus();
            });
        }

        searchInput.addEventListener('focus', () => {
            document.body.classList.add('search-focused');
        });
        searchInput.addEventListener('blur', () => {
            document.body.classList.remove('search-focused');
        });

        // Quick search trigger button
        const quickSearchTrigger = document.getElementById('quick-search-trigger');
        if (quickSearchTrigger) {
            quickSearchTrigger.addEventListener('click', () => {
                searchInput.focus();
                searchInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
            });
        }

        // Type Filter Group
        const typeGroup = document.getElementById('type-filter-group');
        if (typeGroup) {
            typeGroup.addEventListener('click', (e) => {
                const btn = e.target.closest('.filter-type-btn');
                if (!btn) return;
                currentType = btn.getAttribute('data-type');
                typeGroup.querySelectorAll('.filter-type-btn').forEach(b => {
                    b.classList.remove('bg-white', 'text-[#1c2520]', 'shadow-xs');
                    b.classList.add('text-[#55635b]');
                });
                btn.classList.add('bg-white', 'text-[#1c2520]', 'shadow-xs');
                btn.classList.remove('text-[#55635b]');
                filterItems();
            });
        }

        // Status Filter Group
        const statusGroup = document.getElementById('status-filter-group');
        if (statusGroup) {
            statusGroup.addEventListener('click', (e) => {
                const btn = e.target.closest('.filter-status-btn');
                if (!btn) return;
                currentStatus = btn.getAttribute('data-status');
                statusGroup.querySelectorAll('.filter-status-btn').forEach(b => {
                    b.classList.remove('bg-white', 'text-[#1c2520]', 'shadow-xs');
                    b.classList.add('text-[#55635b]');
                });
                btn.classList.add('bg-white', 'text-[#1c2520]', 'shadow-xs');
                btn.classList.remove('text-[#55635b]');
                filterItems();
            });
        }

        // Category Filter Group
        const catGroup = document.getElementById('category-filter-group');
        if (catGroup) {
            catGroup.addEventListener('click', (e) => {
                const btn = e.target.closest('.filter-cat-btn');
                if (!btn) return;
                currentCat = btn.getAttribute('data-cat');
                catGroup.querySelectorAll('.filter-cat-btn').forEach(b => {
                    b.classList.remove('border-[#2d5a43]', 'bg-[#2d5a43]', 'text-white', 'shadow-xs', 'font-medium');
                    b.classList.add('border-[#e6e2d8]', 'bg-white', 'text-[#55635b]', 'font-normal');
                });
                btn.classList.add('border-[#2d5a43]', 'bg-[#2d5a43]', 'text-white', 'shadow-xs', 'font-medium');
                btn.classList.remove('border-[#e6e2d8]', 'bg-white', 'text-[#55635b]', 'font-normal');
                filterItems();
            });
        }

        // Reset Filter function
        function resetFilters() {
            searchInput.value = '';
            currentType = 'all';
            currentStatus = 'all';
            currentCat = 'all';

            if (typeGroup) {
                const defaultTypeBtn = typeGroup.querySelector('.filter-type-btn[data-type="all"]');
                typeGroup.querySelectorAll('.filter-type-btn').forEach(b => b.classList.remove('bg-white', 'text-[#1c2520]', 'shadow-xs'));
                if (defaultTypeBtn) defaultTypeBtn.classList.add('bg-white', 'text-[#1c2520]', 'shadow-xs');
            }

            if (statusGroup) {
                const defaultStatusBtn = statusGroup.querySelector('.filter-status-btn[data-status="all"]');
                statusGroup.querySelectorAll('.filter-status-btn').forEach(b => b.classList.remove('bg-white', 'text-[#1c2520]', 'shadow-xs'));
                if (defaultStatusBtn) defaultStatusBtn.classList.add('bg-white', 'text-[#1c2520]', 'shadow-xs');
            }

            if (catGroup) {
                const defaultCatBtn = catGroup.querySelector('.filter-cat-btn[data-cat="all"]');
                catGroup.querySelectorAll('.filter-cat-btn').forEach(b => {
                    b.classList.remove('border-[#2d5a43]', 'bg-[#2d5a43]', 'text-white', 'shadow-xs', 'font-medium');
                    b.classList.add('border-[#e6e2d8]', 'bg-white', 'text-[#55635b]', 'font-normal');
                });
                if (defaultCatBtn) defaultCatBtn.classList.add('border-[#2d5a43]', 'bg-[#2d5a43]', 'text-white', 'shadow-xs', 'font-medium');
            }

            filterItems();
            showToast('All filters cleared');
        }

        if (resetBtn) resetBtn.addEventListener('click', resetFilters);
        if (emptyResetBtn) emptyResetBtn.addEventListener('click', resetFilters);
    }

    // 4. Keyboard Shortcuts: '/' focuses search, 'Escape' closes modals
    window.addEventListener('keydown', (e) => {
        const searchEl = document.getElementById('search-input');
        if (e.key === '/' && searchEl && document.activeElement !== searchEl && !['input', 'textarea', 'select'].includes(document.activeElement.tagName.toLowerCase())) {
            e.preventDefault();
            searchEl.focus();
            searchEl.select();
        } else if (e.key === 'Escape') {
            closeModals();
        }
    });

    // 5. Interactive Copy Reference with subtle tooltip
    document.addEventListener('click', (e) => {
        const copyBtn = e.target.closest('.copy-ref-btn');
        if (copyBtn) {
            const row = copyBtn.closest('.item-row');
            const ref = row ? row.getAttribute('data-ref') : copyBtn.getAttribute('data-ref');
            if (ref) {
                if (navigator.clipboard) {
                    navigator.clipboard.writeText(ref);
                }
                const tooltip = copyBtn.parentElement.querySelector('.copy-tooltip');
                if (tooltip) {
                    tooltip.classList.remove('opacity-0');
                    setTimeout(() => {
                        tooltip.classList.add('opacity-0');
                    }, 1200);
                }
                showToast(`Copied ${ref} to clipboard`);
            }
        }
    });

    // 6. Modals Logic
    const reportModal = document.getElementById('report-modal');
    const detailsModal = document.getElementById('details-modal');

    function closeModals() {
        if (reportModal) reportModal.classList.add('hidden');
        if (detailsModal) detailsModal.classList.add('hidden');
    }

    // Report modal triggers
    const openReportBtn = document.getElementById('open-report-modal-btn');
    if (openReportBtn) {
        openReportBtn.addEventListener('click', (e) => {
            if (reportModal) {
                e.preventDefault();
                // Set default date to today
                const dateInput = document.getElementById('report-date');
                if (dateInput && !dateInput.value) {
                    dateInput.value = new Date().toISOString().split('T')[0];
                }
                reportModal.classList.remove('hidden');
            } else {
                window.location.href = '/report';
            }
        });
    }

    const closeReportBtn = document.getElementById('close-report-modal');
    if (closeReportBtn) closeReportBtn.addEventListener('click', closeModals);

    const cancelReportBtn = document.getElementById('cancel-report-modal');
    if (cancelReportBtn) cancelReportBtn.addEventListener('click', closeModals);

    const closeDetailsBtn = document.getElementById('close-details-modal');
    if (closeDetailsBtn) closeDetailsBtn.addEventListener('click', closeModals);

    const dismissDetailsBtn = document.getElementById('dismiss-details-modal');
    if (dismissDetailsBtn) dismissDetailsBtn.addEventListener('click', closeModals);

    // Backdrop click to close modals
    [reportModal, detailsModal].forEach(modal => {
        if (modal) {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) closeModals();
            });
        }
    });

    // 7. Item Actions (View Details / Claim Item / Report Match)
    document.addEventListener('click', (e) => {
        const viewBtn = e.target.closest('.view-details-btn');
        const claimBtn = e.target.closest('.claim-item-btn');
        const matchBtn = e.target.closest('.report-match-btn');

        if (viewBtn || claimBtn || matchBtn) {
            const row = (viewBtn || claimBtn || matchBtn).closest('.item-row');
            if (!row) return;

            const ref = row.getAttribute('data-ref') || 'REC-000';
            const name = row.getAttribute('data-name') || 'Item';
            const cat = row.getAttribute('data-cat') || '-';
            const location = row.getAttribute('data-location') || '-';
            const date = row.getAttribute('data-date') || '-';
            const type = (row.getAttribute('data-type') || 'FOUND').toUpperCase();
            const status = row.getAttribute('data-status') || 'Open';
            const desc = row.getAttribute('data-desc') || '';
            const url = row.getAttribute('data-url') || '#';

            if (claimBtn) {
                // If claim button clicked directly, navigate to item detail or open modal
                window.location.href = url;
                return;
            }

            if (matchBtn) {
                showToast(`Match reported for ${ref}. Redirecting to details...`);
                setTimeout(() => { window.location.href = url; }, 500);
                return;
            }

            // Populate view details modal
            if (detailsModal) {
                const refTag = document.getElementById('modal-ref-tag');
                const copyRef = document.getElementById('modal-copy-ref');
                const itemName = document.getElementById('modal-item-name');
                const categoryEl = document.getElementById('modal-category');
                const locationEl = document.getElementById('modal-location');
                const dateEl = document.getElementById('modal-date');
                const statusEl = document.getElementById('modal-status');
                const descEl = document.getElementById('modal-desc');
                const permalink = document.getElementById('modal-permalink');
                const actionBtn = document.getElementById('modal-action-btn');
                const typeBadge = document.getElementById('modal-type-badge');

                if (refTag) refTag.textContent = ref;
                if (copyRef) copyRef.textContent = ref;
                if (itemName) itemName.textContent = name;
                if (categoryEl) categoryEl.textContent = cat;
                if (locationEl) locationEl.textContent = location;
                if (dateEl) dateEl.textContent = date;
                if (statusEl) statusEl.textContent = status;
                if (descEl) descEl.textContent = desc || 'No additional description provided.';
                if (permalink) permalink.href = url;

                if (typeBadge) {
                    typeBadge.textContent = type;
                    if (type === 'FOUND') {
                        typeBadge.className = 'px-2 py-0.5 rounded font-mono text-[11px] font-medium bg-[#edf6f0] text-[#23643b] border border-[#c6e3cf]';
                    } else {
                        typeBadge.className = 'px-2 py-0.5 rounded font-mono text-[11px] font-medium bg-[#fdf5f0] text-[#c85a32] border border-[#f5d6c8]';
                    }
                }

                if (actionBtn) {
                    if (status.toLowerCase() === 'claimed') {
                        actionBtn.textContent = 'Claimed / Resolved';
                        actionBtn.disabled = true;
                        actionBtn.className = 'px-3.5 py-1.5 rounded bg-[#e6e2d8] text-[#7e8c84] font-medium text-xs cursor-not-allowed';
                    } else if (type === 'FOUND') {
                        actionBtn.textContent = 'Claim Item';
                        actionBtn.disabled = false;
                        actionBtn.className = 'px-3.5 py-1.5 rounded bg-[#2d5a43] hover:bg-[#143426] text-white font-medium shadow-xs transition-all duration-150 ease-out hover:-translate-y-[1px] text-xs';
                        actionBtn.onclick = () => { window.location.href = url; };
                    } else {
                        actionBtn.textContent = 'Report Match';
                        actionBtn.disabled = false;
                        actionBtn.className = 'px-3.5 py-1.5 rounded bg-[#c85a32] hover:bg-[#b94e27] text-white font-medium shadow-xs transition-all duration-150 ease-out hover:-translate-y-[1px] text-xs';
                        actionBtn.onclick = () => { window.location.href = url; };
                    }
                }

                detailsModal.classList.remove('hidden');
            }
        }
    });

    // 8. Photo Preview on File Input
    const photoInput = document.getElementById('report-photo') || document.getElementById('photoInput');
    const imagePreview = document.getElementById('imagePreview');
    if (photoInput && imagePreview) {
        photoInput.addEventListener('change', () => {
            const file = photoInput.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = e => {
                    imagePreview.src = e.target.result;
                    imagePreview.classList.remove('hidden');
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // 9. Claim form accordion on detail page
    const claimToggle = document.getElementById('claimToggle');
    const claimSection = document.getElementById('claimSection');
    if (claimToggle && claimSection) {
        claimToggle.addEventListener('click', () => {
            claimSection.classList.toggle('hidden');
            if (!claimSection.classList.contains('hidden')) {
                claimSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
        });
    }
})();
