.PHONY: format check-format lint

# Format code with black
format:
	black .

# Check if the code is correctly formatted with black
check-format:
	black --check .

# Lint code with flake8
lint:
	flake8 .
