# Testing

Frontend tests use Vitest, jsdom and React Testing Library. The included tests cover the homepage render and pure median/accuracy helper calculations. They do not yet cover every game transition or real camera hardware.

Backend tests use pytest and FastAPI TestClient/HTTPX. They cover health, game configuration, accepted summaries, invalid scores, unknown game identifiers, duplicate game summaries and rejected extra fields.

Run commands in the README. Only report checks as passed when they have actually run in the target environment.
