#!/bin/bash


# Defining color constans for outputs
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color


# Usage
function show_usage {
  echo -e "${YELLOW}Usage:${NC}"
  echo -e "  ./run.sh [options]"
  echo
  echo -e "${YELLOW}Options:${NC}"
  echo -e "  --app, -a       Run the application"
  echo -e "  --test, -t      Run the tests"
  echo -e "  --help, -h      Show this help message"
  echo
  echo -e "${YELLOW}Examples:${NC}"
  echo -e "  .run.sh -a      # Run the application only"
  echo -e "  .run.sh -t      # Run tests only"
  echo -e "  .run.sh -a -t   # Run both application and tests"
  echo -e "  .run.sh         # Without arguments, runs application by default"
}


# run application function
function run_app {
  echo -e "${GREEN}Running application...${NC}"
  python -m src.main
}

# Function to run the tests
function run_tests {
  echo -e "${GREEN}Running tests...${NC}"
  pytest
}

# Dfault behavior when no arguments are provided
if [ $# -eq 0 ]; then
  run_app
  exit 0
fi


# Process command line arguments
RUN_APP=false
RUN_TESTS=false

while [[ $# -gt 0 ]]; do
  case "$1" in
      --app|-a)
          RUN_APP=true
          shift
          ;;
      --test|-t)
          RUN_TESTS=true
          shift
          ;;
      --help|-h)
          show_usage
          exit 0
          ;;
      *)
        echo -e "${RED}Unknown option: $1${NC}"
        show_usage
        exit 1
        ;;
  esac
done


# Execute based on arguments provided
if $RUN_APP; then
  run_app
fi


if $RUN_TESTS; then
  run_app
fi

exit 0
