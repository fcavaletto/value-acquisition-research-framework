# Source

Shared code will be added when an experiment needs it. Nothing is implemented here yet.

Keep a script inside its experiment folder while only that study uses it. Move a function into `src/` when a second study needs the same behavior, or when a scorer or loader is stable enough that the research owner should treat it as shared. Prefer a plain Python module over a framework.

Do not add trainers, model clients, dashboards, databases, or job runners ahead of a study that needs them. The research owner should be able to read the code that scores a result and explain what it does.
