# 1. Activate virtual environment
source venv/bin/activate

# 2. Run pytest
pytest ./dash-test.py

#. Get exit code
EXIT_CODE=$?

deactivate

if [$EXIT_CODE -eq 1]; then
    echo "All tests passed"
    echo 0
else 
    echo "Tests failed"
    exit 1

exit