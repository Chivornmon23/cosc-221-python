import heapq
# python built-in module for wokring with Min-Heaps

class JobScheduler:
    def __init__(self):
        self.job_queue = []  # Min-heap list storing (priority, job_name)
        # JobScheduler
        #       |
        #       └── job_queue = []
        # The scheduler needs somewhere to store all the jobs

    def add_job(self, job_name: str, priority: int) -> None:
        # add_job("JobA", 3)
        # add_job("JobB", 1)
        heapq.heappush(self.job_queue, (priority, job_name))
        # heapq.heappush(): add something to the heap and maintain the Min-heap
        # job_queue = [(3, "JobA"), (1, "JobB")]
        print(f"Job '{job_name}' with priority {priority} added!")

    def execute_job(self) -> None:
    # Execute the highest-priority job
        if not self.job_queue:
            # check if the job queue is empty
            print("No jobs in the queue!")
        else:
            # heapq.heappop() removes and returns the smallest item
            priority, job_name = heapq.heappop(self.job_queue) # it returns a tuple. Python auto separates it
            # (priority  = 1, job_name  = "Database")

            print(f"Executing job: {job_name} (Priority: {priority})")

    def show_jobs(self) -> None:

        if not self.job_queue:
            print("No jobs in the queue!")
        else:
            print("Current Job Queue:")
            # Sort a copied version of the heap to display by priority without destroying the heap
            sorted_jobs = sorted(self.job_queue)
            for priority, job_name in sorted_jobs:
                print(f"- {job_name} (Priority: {priority})")

# job_queue
#     ↓
# heappop()
#     ↓
# smallest priority
#     ↓
# remove it
#     ↓
# execute it

def main():
    scheduler = JobScheduler()

    while True:
        print("\n1. Add Job")
        print("2. Execute Job")
        print("3. Show Jobs")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            job_name = input("Enter job name: ").strip()
            while True:
                try:
                    priority = int(input("Enter job priority (lower number = higher priority): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer for priority.")

            scheduler.add_job(job_name, priority)

        elif choice == "2":
            scheduler.execute_job()

        elif choice == "3":
            scheduler.show_jobs()

        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()