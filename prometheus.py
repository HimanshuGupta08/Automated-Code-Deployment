from prometheus_client import start_http_server, Counter
import time

# Create a Prometheus metric to track workflow runs
workflow_runs_counter = Counter('github_actions_workflow_runs', 'Total number of GitHub Actions workflow runs')

def count_workflow_runs():
    # Increment the counter when a workflow run occurs (or some other event)
    workflow_runs_counter.inc()

if __name__ == '__main__':
    start_http_server(8000)  # Start an HTTP server on port 8000
    while True:
        count_workflow_runs()  # This would be triggered by your GitHub Actions workflow
        time.sleep(60)  # Update every 60 seconds or based on your use case
