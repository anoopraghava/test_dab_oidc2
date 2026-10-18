import sys
from datetime import datetime

print(f"Hello from Azure Databricks Asset Bundles - using OIDC!")
print(f"Job executed successfully at: {datetime.now().isoformat()}")
print(f"Python version: {sys.version}")