"CANDIDATES "
class VotingSystem:
    def __init__(self):
        self.candidates = {}
        self.votes = {}

    def add_candidate(self, candidate_name):
        if candidate_name in self.candidates:
            print(f"Candidate {candidate_name} already exists.")
        else:
            self.candidates[candidate_name] = 0
            self.votes[candidate_name] = 0
            print(f"Candidate {candidate_name} added.")

    def cast_vote(self, candidate_name):
        if candidate_name not in self.candidates:
            print(f"Candidate {candidate_name} does not exist.")
        else:
            self.candidates[candidate_name] += 1
            print(f"Vote casted for {candidate_name}.")

    def show_results(self):
        print("Election Results:")
        for candidate, vote_count in self.candidates.items():
            print(f"{candidate}: {vote_count} votes")

def main():
    system = VotingSystem()

    while True:
        print("\nVoting System Menu:")
        print("1. Add Candidate")
        print("2. Cast Vote")
        print("3. Show Results")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            candidate_name = input("Enter the candidate's name: ")
            system.add_candidate(candidate_name)
        elif choice == '2':
            candidate_name = input("Enter the candidate's name to vote for: ")
            system.cast_vote(candidate_name)
        elif choice == '3':
            system.show_results()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
