# Contributing to S.Y.N.A.P.S.E

## 🎯 Development Workflow

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes with tests
3. Run quality checks: `pre-commit run --all-files`
4. Run tests: `pytest`
5. Commit with conventional commit message
6. Push and create a Pull Request

## 📏 Code Standards

- **Python**: 3.11+
- **Line length**: 100 characters
- **Type hints**: Required for all public functions
- **Test coverage**: Minimum 85%
- **Documentation**: Docstrings for all public APIs

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/synapse --cov-report=html

# Run specific test type
pytest -m unit
pytest -m integration
```

## 📝 Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance
