#!/bin/bash
#
# tests.sh
# Run all tests for LeetCode solutions (Python and Swift)
#
# Author: Illya Starikov
# License: MIT
#

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Running All LeetCode Tests${NC}"
echo "============================================="

# Track overall results
total_test_files=0
passed_test_files=0
failed_test_files=()

# Python test results
python_total=0
python_passed=0
python_failed=()

# Swift test results
swift_total=0
swift_passed=0
swift_failed=()

# Run Python tests
echo ""
echo -e "${YELLOW}📘 Python Tests${NC}"
echo "-----------------------------------"

if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo -e "${RED}❌ Python not found${NC}"
    exit 1
fi

# Check if pytest is available
if $PYTHON_CMD -m pytest --version &> /dev/null; then
    echo "Using pytest for Python tests..."
    echo ""
    
    # Run pytest on all Python test files
    $PYTHON_CMD -m pytest *_test.py -v --tb=short
    pytest_exit_code=$?
    
    # Count Python test files
    for test_file in *_test.py; do
        if [[ -f "$test_file" ]]; then
            python_total=$((python_total + 1))
            total_test_files=$((total_test_files + 1))
            
            if [[ $pytest_exit_code -eq 0 ]]; then
                python_passed=$((python_passed + 1))
                passed_test_files=$((passed_test_files + 1))
            else
                # For pytest, we can't determine individual file failures easily
                # so we'll mark all as potentially failed if any fail
                python_failed+=("$test_file")
                failed_test_files+=("Python: $test_file")
            fi
        fi
    done
    
    # If pytest failed, adjust the count
    if [[ $pytest_exit_code -ne 0 ]]; then
        python_passed=0
        python_failed=()
        for test_file in *_test.py; do
            if [[ -f "$test_file" ]]; then
                python_failed+=("$test_file")
            fi
        done
        passed_test_files=$((passed_test_files - python_total))
    fi
else
    echo "pytest not found, using unittest..."
    echo ""
    
    # Run each Python test file individually
    for test_file in *_test.py; do
        if [[ -f "$test_file" ]]; then
            echo -e "${BLUE}▶ Running: $test_file${NC}"
            
            $PYTHON_CMD -m unittest "$test_file" 2>&1 | tail -n 1
            exit_code=${PIPESTATUS[0]}
            
            python_total=$((python_total + 1))
            total_test_files=$((total_test_files + 1))
            
            if [[ $exit_code -eq 0 ]]; then
                python_passed=$((python_passed + 1))
                passed_test_files=$((passed_test_files + 1))
                echo -e "${GREEN}✅ $test_file passed${NC}"
            else
                python_failed+=("$test_file")
                failed_test_files+=("Python: $test_file")
                echo -e "${RED}❌ $test_file failed${NC}"
            fi
            echo ""
        fi
    done
fi

# Run Swift tests
echo ""
echo -e "${YELLOW}🍎 Swift Tests${NC}"
echo "-----------------------------------"

if ! command -v swift &> /dev/null; then
    echo -e "${YELLOW}⚠️  Swift not installed, skipping Swift tests${NC}"
else
    for test_file in *_test.swift; do
        if [[ -f "$test_file" ]]; then
            echo ""
            echo -e "${BLUE}▶ Running: $test_file${NC}"
            
            # Run the test and capture output
            output=$(swift "$test_file" 2>&1)
            exit_code=$?
            
            # Show the test output
            echo "$output" | grep -E "^(▶|✅|❌|📊|==== Test Results ====)"
            
            swift_total=$((swift_total + 1))
            total_test_files=$((total_test_files + 1))
            
            if [[ $exit_code -eq 0 ]]; then
                swift_passed=$((swift_passed + 1))
                passed_test_files=$((passed_test_files + 1))
                echo -e "${GREEN}✅ $test_file passed${NC}"
            else
                swift_failed+=("$test_file")
                failed_test_files+=("Swift: $test_file")
                echo -e "${RED}❌ $test_file failed${NC}"
            fi
        fi
    done
fi

# Print summary
echo ""
echo "============================================="
echo -e "${BLUE}📊 Test Summary${NC}"
echo "============================================="

# Python summary
if [[ $python_total -gt 0 ]]; then
    echo ""
    echo -e "${YELLOW}Python Tests:${NC}"
    echo "  Total: $python_total"
    echo -e "  ${GREEN}Passed: $python_passed${NC}"
    echo -e "  ${RED}Failed: ${#python_failed[@]}${NC}"
    
    if [[ ${#python_failed[@]} -gt 0 ]]; then
        echo "  Failed files:"
        for failed in "${python_failed[@]}"; do
            echo -e "    ${RED}❌ $failed${NC}"
        done
    fi
fi

# Swift summary
if [[ $swift_total -gt 0 ]]; then
    echo ""
    echo -e "${YELLOW}Swift Tests:${NC}"
    echo "  Total: $swift_total"
    echo -e "  ${GREEN}Passed: $swift_passed${NC}"
    echo -e "  ${RED}Failed: ${#swift_failed[@]}${NC}"
    
    if [[ ${#swift_failed[@]} -gt 0 ]]; then
        echo "  Failed files:"
        for failed in "${swift_failed[@]}"; do
            echo -e "    ${RED}❌ $failed${NC}"
        done
    fi
fi

# Overall summary
echo ""
echo -e "${BLUE}Overall:${NC}"
echo "  Total test files: $total_test_files"
echo -e "  ${GREEN}Passed: $passed_test_files${NC}"
echo -e "  ${RED}Failed: ${#failed_test_files[@]}${NC}"

if [[ ${#failed_test_files[@]} -gt 0 ]]; then
    echo ""
    echo -e "${RED}⚠️  Some tests failed!${NC}"
    exit 1
else
    echo ""
    # Print pytest-style green success bar
    echo -e "${GREEN}======================== All tests passed ========================${NC}"
    echo ""
    exit 0
fi