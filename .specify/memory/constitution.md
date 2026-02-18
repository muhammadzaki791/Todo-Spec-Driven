<!-- Sync Impact Report:
Version change: N/A → 1.0.0
List of modified principles: N/A (initial constitution)
Added sections: All principles and sections (initial constitution)
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md ✅ (compatible with new constitution)
  - .specify/templates/spec-template.md ✅ (compatible with new constitution)
  - .specify/templates/tasks-template.md ✅ (compatible with new constitution)
Follow-up TODOs: None
-->

# In-Memory Todo Console Application Constitution

## Core Principles

### Spec-Driven Development
All functionality must originate from written specifications following the spec → plan → tasks → implementation workflow. Each iteration must update or reference a spec file to ensure traceability and maintainability.

### Agentic Autonomy
Claude Code writes all production code without manual intervention. No manual code edits by the developer - all changes must be made through the agentic workflow to ensure consistency and adherence to spec-driven principles.

### Simplicity and Clarity
Maintain beginner-friendly console UX with clean, readable code following Python PEP 8 conventions. Focus on modular and readable project structure that is easy to understand and maintain.

### Deterministic Behavior
All data remains in memory during runtime only - no databases, files, or external storage. Ensure pure in-memory state management for predictable and consistent application behavior.

### Functional Completeness
Implement all 5 basic todo features: add, view, update, delete, and mark complete/incomplete. All functionality must work without errors and follow clean Python conventions.

### Clean Code Standards
Code must follow clean Python conventions (PEP 8) with modular and readable project structure. All code must be maintainable, testable, and logically structured for future enhancements.

## Technical Constraints

Language: Python 3.13+, Environment management: UV, Interface: Command-line (console only), No databases, files, or external storage, No third-party task management libraries.

## Development Workflow

No manual code edits by the developer, All functionality must originate from written specifications, Each iteration must update or reference a spec file, Code must follow clean Python conventions (PEP 8), Modular and readable project structure.

## Governance

All implementations must follow spec → plan → tasks → implementation workflow; Constitution supersedes all other practices; Amendments require documentation and approval; All changes must be agentic (no manual code editing); Code reviews must verify compliance with all principles.

**Version**: 1.0.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04