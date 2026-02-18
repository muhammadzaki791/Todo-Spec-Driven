---
description: "Task list for Todo Console Application"
---

# Tasks: Todo Console Application

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Create src/ directory with models/, services/, cli/ subdirectories
- [X] T003 [P] Create placeholder README.md and CLAUDE.md files

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Define Todo data model with ID, title, description, and completion status in src/models/todo.py
- [X] T005 Create TodoList collection structure in memory using dictionary in src/models/todo.py
- [X] T006 [P] Create todo_service.py in src/services/ for core business logic
- [X] T007 Create basic CLI structure in src/cli/main.py to handle user commands
- [X] T008 [P] Configure UV environment for Python 3.13+ with pyproject.toml

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Items (Priority: P1) 🎯 MVP

**Goal**: Users can create new todo items with basic information to track their tasks

**Independent Test**: Can be fully tested by running the application and adding a new task, then verifying it appears in the system with a unique ID and correct details.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T009 [P] [US1] Create unit tests for add functionality in tests/unit/test_todo.py

### Implementation for User Story 1

- [X] T010 [P] [US1] Implement Todo class with validation rules in src/models/todo.py
- [X] T011 [US1] Implement add_todo method in TodoService in src/services/todo_service.py
- [X] T012 [US1] Implement unique ID generation strategy in src/services/todo_service.py
- [X] T013 [US1] Add command handling for 'add' in src/cli/main.py
- [X] T014 [US1] Add validation for required title and optional description in src/services/todo_service.py
- [X] T015 [US1] Add success message display after adding todo in src/cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todo Items (Priority: P1)

**Goal**: Users can see all their todo items with their current status to understand what tasks they have to complete

**Independent Test**: Can be fully tested by adding some tasks and then viewing the complete list to verify all tasks are displayed with correct information.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T016 [P] [US2] Create unit tests for view functionality in tests/unit/test_todo.py

### Implementation for User Story 2

- [X] T017 [P] [US2] Implement get_all_todos method in TodoService in src/services/todo_service.py
- [X] T018 [US2] Implement display format for todo items with ID, title, description, and completion status in src/cli/main.py
- [X] T019 [US2] Add command handling for 'view' in src/cli/main.py
- [X] T020 [US2] Handle empty todo list case with appropriate message in src/cli/main.py
- [X] T021 [US2] Implement clear status indicator for completion status in display in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update and Manage Todo Items (Priority: P2)

**Goal**: Users can modify existing todo items and manage their status to keep their task list current and accurate

**Independent Test**: Can be fully tested by creating a task, updating its details, and marking it complete/incomplete to verify the changes persist correctly.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T022 [P] [US3] Create unit tests for update and complete/incomplete functionality in tests/unit/test_todo.py

### Implementation for User Story 3

- [X] T023 [P] [US3] Implement update_todo method in TodoService in src/services/todo_service.py
- [X] T024 [P] [US3] Implement mark_complete and mark_incomplete methods in TodoService in src/services/todo_service.py
- [X] T025 [US3] Add command handling for 'update' in src/cli/main.py
- [X] T026 [US3] Add command handling for 'complete' and 'incomplete' in src/cli/main.py
- [X] T027 [US3] Add validation for existing todo ID before update in src/services/todo_service.py
- [X] T028 [US3] Update display to reflect status changes in subsequent views in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Todo Items (Priority: P2)

**Goal**: Users can remove completed or unwanted tasks from their list to keep their todo list manageable and relevant

**Independent Test**: Can be fully tested by creating a task, deleting it, and then attempting to view it to confirm it no longer exists.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T029 [P] [US4] Create unit tests for delete functionality in tests/unit/test_todo.py

### Implementation for User Story 4

- [X] T030 [P] [US4] Implement delete_todo method in TodoService in src/services/todo_service.py
- [X] T031 [US4] Add command handling for 'delete' in src/cli/main.py
- [X] T032 [US4] Add validation for existing todo ID before deletion in src/services/todo_service.py
- [X] T033 [US4] Add confirmation message after successful deletion in src/cli/main.py
- [X] T034 [US4] Ensure deleted task no longer appears in view operations in src/services/todo_service.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Command-Line Interaction Loop & Error Handling

**Goal**: Implement the main application loop and comprehensive error handling

- [X] T035 Implement main command loop in src/cli/main.py to keep application running
- [X] T036 Add command routing from user input to corresponding service methods in src/cli/main.py
- [X] T037 Handle invalid menu selections gracefully in src/cli/main.py
- [X] T038 Handle invalid or missing input gracefully in src/cli/main.py
- [X] T039 Add exit command functionality in src/cli/main.py
- [X] T040 Implement error handling for invalid ID cases in src/services/todo_service.py
- [X] T041 Add validation for non-existent todos in update, delete, and complete operations in src/services/todo_service.py
- [X] T042 Ensure app does not crash on bad input in src/cli/main.py

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T043 [P] Add input validation for very long titles or descriptions in src/services/todo_service.py
- [X] T044 [P] Add maximum length validation per data model (200 chars for title, 1000 for description) in src/models/todo.py
- [X] T045 Code cleanup and refactoring for readability
- [X] T046 [P] Documentation updates in docstrings for all classes and methods
- [X] T047 [P] Additional unit tests (if requested) in tests/unit/test_todo.py
- [X] T048 Run quickstart.md validation to ensure all commands work as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Interaction Loop & Error Handling (Phase 7)**: Can run after foundational phase
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before CLI interface
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Create unit tests for add functionality in tests/unit/test_todo.py"
Task: "Implement Todo class with validation rules in src/models/todo.py"
Task: "Implement add_todo method in TodoService in src/services/todo_service.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add Interaction Loop & Error Handling → Test → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence