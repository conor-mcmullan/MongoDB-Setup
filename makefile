# Define variables
PYTHON=python
SCRIPTS_DIR=Scripts
DATA_DIR=Data/db
LOGS_DIR=Logs
MONGOD_CONFIG=Config/mongod.conf

# Targets
.PHONY: all reset start_mongo clean

# Default target
all: help

# Help target
help:
	@echo "Makefile Commands:"
	@echo "  make reset       - Wipe the Data/db directory and truncate the mongod.log file"
	@echo "  make start_mongo - Start the MongoDB server with the specified configuration"
	@echo "  make clean      - Remove all files in Data/db except README.md"

# Reset target
reset:
	$(PYTHON) $(SCRIPTS_DIR)/reset.py

# Start MongoDB target
start_mongo:
	mongod --config $(MONGOD_CONFIG)

# Clean target
clean:
	@echo "Cleaning the Data/db directory..."
	find $(DATA_DIR) -type f ! -name 'README.md' -delete
	@echo "Cleaned the Data/db directory."

