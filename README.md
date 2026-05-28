# Simple Calculator Project  
A Hands-On Introduction to Git and Test-Driven Development (TDD)

You will work in small teams and use TDD to guide feature development. 
Each team member will contribute code on separate branches, 
then merge changes together, 
resolving any conflicts as needed.

---

## Objectives
- Practice forking and cloning a repository.
- Create and use feature branches.
- Write small, clean commits with clear messages.
- Use TDD to implement calculator functionality step by step.
- Experience and resolve merge conflicts.
- Collaborate through pull requests.

---

## Required Tools
- Git (command line or GUI)
- GitHub or another Git hosting service
- A code editor
- A supported programming language runtime (Python 3)

---

## Workflow Summary
You will follow a structured, repeatable workflow:

1. **Fork** this repository.
2. **Clone** your fork to your local machine.
3. Create a new **branch** for each task.
4. Start each task by writing a **failing test**.
5. Write the minimal amount of code to make the test **pass**.
6. **Refactor** as needed.
7. Commit frequently with descriptive messages.
8. Push your branch and open a **pull request**.
9. Collaborate with teammates, review each other’s changes, and merge responsibly.

---

## Suggested Tasks
Your instructor may assign tasks or let you choose. Common options:

### Core Tasks
- Implement `add()`  
- Implement `subtract()`  
- Implement `multiply()`
- Implement `divide()`
- Implement `multiply_by_add()` (using successive calls to `add()`)
- Implement `divide_by_subtract()` (using successive calls to `subtract()`)
- Implement `exponent()`
- Implement `modulo()`

### Validation Tasks
- Reject non-numeric input  
- Support integer and decimal inputs  

### Stretch Tasks (Optional)
- Add a history log  
- Add command-line flags or menu options  

**Each task is performed on its own feature branch!**

---

## Team Collaboration Guidelines
- Before merging, always review tests and code together.
- Do not work on `main` directly.
- When conflicts occur, resolve them as a team rather than individually.
- Keep pull requests small and focused on a single task.

---

## TDD Cycle (Required)
For every feature, follow this sequence:

1. **Red** – Write a new test that fails.  
2. **Green** – Implement the minimal code required to pass the test.  
3. **Refactor** – Improve clarity and structure without changing behavior.

Repeat this cycle for all tasks.

