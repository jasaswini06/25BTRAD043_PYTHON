{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "aa244413",
   "metadata": {},
   "source": [
    "Name: Jasaswini Sahu\n",
    "\n",
    "USN: 25BTRAD043\n",
    "\n",
    "Experiment Part 3"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8b6522df",
   "metadata": {},
   "source": [
    "Lab Exercise 8 — Contact Book Using Lists and Dictionaries\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7d157d58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "1. Add  2. Search  3. Update  4. Delete  5. Display  6. Exit\n",
      "Invalid choice.\n",
      "\n",
      "1. Add  2. Search  3. Update  4. Delete  5. Display  6. Exit\n",
      "Contact added.\n",
      "\n",
      "1. Add  2. Search  3. Update  4. Delete  5. Display  6. Exit\n",
      "Invalid choice.\n",
      "\n",
      "1. Add  2. Search  3. Update  4. Delete  5. Display  6. Exit\n",
      "All contacts:\n",
      "1 - jasaswini sahu\n",
      "\n",
      "1. Add  2. Search  3. Update  4. Delete  5. Display  6. Exit\n",
      "Contact book closed.\n"
     ]
    }
   ],
   "source": [
    "contacts = []\n",
    "\n",
    "while True:\n",
    "    print(\"\\n1. Add  2. Search  3. Update  4. Delete  5. Display  6. Exit\")\n",
    "    choice = input(\"Enter choice: \").strip()\n",
    "\n",
    "    if choice == \"6\":\n",
    "        print(\"Contact book closed.\")\n",
    "        break\n",
    "\n",
    "    if choice == \"5\":\n",
    "        if not contacts:\n",
    "            print(\"Contact book is empty.\")\n",
    "        else:\n",
    "            print(\"All contacts:\")\n",
    "            for contact in contacts:\n",
    "                print(f\"{contact['name']} - {contact['phone']}\")\n",
    "        continue\n",
    "\n",
    "    if choice not in (\"1\", \"2\", \"3\", \"4\"):\n",
    "        print(\"Invalid choice.\")\n",
    "        continue\n",
    "\n",
    "    name = input(\"Enter name: \").strip()\n",
    "    if not name:\n",
    "        print(\"Name cannot be empty.\")\n",
    "        continue\n",
    "\n",
    "    found = None\n",
    "    for contact in contacts:\n",
    "        if contact[\"name\"].lower() == name.lower():\n",
    "            found = contact\n",
    "            break\n",
    "\n",
    "    if choice == \"1\":\n",
    "        if found is not None:\n",
    "            print(\"A contact with that name already exists.\")\n",
    "        else:\n",
    "            phone = input(\"Enter phone number: \").strip()\n",
    "            contacts.append({\"name\": name, \"phone\": phone})\n",
    "            print(\"Contact added.\")\n",
    "\n",
    "    elif found is None:\n",
    "        print(\"Contact not found.\")\n",
    "\n",
    "    elif choice == \"2\":\n",
    "        print(f\"{found['name']} - {found['phone']}\")\n",
    "\n",
    "    elif choice == \"3\":\n",
    "        found[\"phone\"] = input(\"Enter new phone number: \").strip()\n",
    "        print(\"Contact updated.\")\n",
    "\n",
    "    elif choice == \"4\":\n",
    "        contacts.remove(found)\n",
    "        print(\"Contact deleted.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "557ca996",
   "metadata": {},
   "source": [
    "Lab Exercise 9 — Student Grading System\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1d13c7ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Student Results\n",
      "jasaswini sahu - 100/100 - Grade A\n"
     ]
    }
   ],
   "source": [
    "students = {}\n",
    "total = int(input(\"Enter number of students: \"))\n",
    "\n",
    "while len(students) < total:\n",
    "    name = input(\"Enter student name: \").strip()\n",
    "    if not name or name in students:\n",
    "        print(\"Enter a non-empty, unique name.\")\n",
    "        continue\n",
    "\n",
    "    try:\n",
    "        marks = int(input(\"Enter marks out of 100: \"))\n",
    "    except ValueError:\n",
    "        print(\"Enter marks as a whole number.\")\n",
    "        continue\n",
    "\n",
    "    if not 0 <= marks <= 100:\n",
    "        print(\"Marks must be between 0 and 100.\")\n",
    "        continue\n",
    "\n",
    "    students[name] = marks\n",
    "\n",
    "print(\"\\nStudent Results\")\n",
    "for name, marks in students.items():\n",
    "    if marks >= 90:\n",
    "        grade = \"A\"\n",
    "    elif marks >= 75:\n",
    "        grade = \"B\"\n",
    "    elif marks >= 60:\n",
    "        grade = \"C\"\n",
    "    elif marks >= 40:\n",
    "        grade = \"D\"\n",
    "    else:\n",
    "        grade = \"F\"\n",
    "\n",
    "    print(f\"{name} - {marks}/100 - Grade {grade}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "232d7e90",
   "metadata": {},
   "source": [
    "Lab Exercise 10 — Frequency Counter Using Dictionaries\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "14657754",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Word frequencies\n",
      "good - 1\n"
     ]
    }
   ],
   "source": [
    "text = input(\"Enter a sentence or survey responses: \").lower()\n",
    "\n",
    "# Replace common punctuation with spaces before splitting.\n",
    "for symbol in \",.!?;:\":\n",
    "    text = text.replace(symbol, \" \")\n",
    "\n",
    "words = text.split()\n",
    "frequency = {}\n",
    "\n",
    "for word in words:\n",
    "    frequency[word] = frequency.get(word, 0) + 1\n",
    "\n",
    "print(\"\\nWord frequencies\")\n",
    "for word, count in frequency.items():\n",
    "    print(f\"{word} - {count}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv (3.9.6)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
