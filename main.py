# =============================================================================
# OmniCo Confidential
# -------------------
# This source code contains proprietary information of OmniCo.
# =============================================================================

def main():
    # Initialize the stats dictionary for each algorithm
    stats = {
        'JoyStream': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0,
            'avg_happiness' : 0
        },
        'SerenityFlow': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0,
            'avg_happiness': 0
        },
        'DeepPulse': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0,
            'avg_happiness': 0
        }
    }

    # Open the CSV file and read data
    with open('euphoria_data.csv', 'r') as file:
        # Skip the header line
        header = file.readline()

        # Read each line in the file
        for line in file:
            # Remove any trailing whitespace characters like newline
            line = line.strip()

            # Split the line into a list of values
            columns = line.split(',')

            # Assign each column to a variable
            user_id = columns[0]
            algorithm = columns[1]

            session_duration = int(columns[2])
            happiness_rating = int(columns[3])

            # Update stats based on the algorithm
            if algorithm in stats:
                stats[algorithm]['total_happiness'] += happiness_rating
                stats[algorithm]['total_duration'] += session_duration
                stats[algorithm]['session_count'] += 1
            else:
                # Handle any unexpected algorithm names
                print(f"Unknown algorithm: {algorithm}")
            

    # TODO: Calculate averages for each algorithm
    # For each algorithm in the stats dictionary:
    #   - Calculate avg_happiness = total_happiness / session_count
    #   - Calculate avg_duration = total_duration / session_count
    #   - Store these back into the stats dictionary under 'avg_happiness' and 'avg_duration'
    for algorithm, stat in stats.items():
        stat['avg_happiness'] = stat['total_happiness']/stat['session_count']
    for algorithm, stat in stats.items():
        stat['avg_duration'] = stat['total_duration'] / stat['session_count']

    # TODO: Determine the algorithm with the highest average happiness rating
    # Initialize variables to keep track of the highest average happiness and the corresponding algorithm
    # Loop through stats to compare avg_happiness values
    max_avg_happiness = 0
    max_hap_algorithm = "Blank"
    for algorithm, stat in stats.items():
        if stat['avg_happiness'] > max_avg_happiness:
            max_avg_happiness = stat['avg_happiness']
            max_hap_algorithm = algorithm

    # TODO: Determine the algorithm with the longest average session duration
    # Initialize variables to keep track of the longest average duration and the corresponding algorithm
    # Loop through stats to compare avg_duration values
    max_avg_duration = 0
    max_dur_algorithm = 0
    for algorithm, stat in stats.items():
        if stat['avg_duration'] > max_avg_duration:
            max_avg_duration = stat['avg_duration']
            max_dur_algorithm = algorithm

    # TODO: Print the report
    # Use print statements to display the results in a formatted way
    # Follow the structure provided in the example output
    print("")
    print("Euphoria User Engagement Analysis Report")
    print("----------------------------------------")
    print("")
    print("Average Happiness Rating per Algorithm:")
    for algorithm, stat in stats.items():
        stat['avg_happiness'] = stat['total_happiness']/stat['session_count']
        print(f"-{algorithm}: {stat['avg_happiness']} ")
    print("")
    print("Total Number of Sessions per Algorithm:")
    for algorithm, stat in stats.items():
        print(f"-{algorithm}: {stat['session_count']}")
    print("")
    print("Average Session Duration per Algorithm:")
    for algorithm, stat in stats.items():
        stat['avg_duration'] = stat['total_duration'] / stat['session_count']
        print(f"-{algorithm}: {stat['avg_duration']} minutes")
    print("")
    print("Highest Average Happiness Rating:")
    print(f"-{max_hap_algorithm} with an average happiness rating of {max_avg_happiness}")
    print("")
    print("Longest Average Session Duration:")
    print(f"-{max_dur_algorithm} with an average session duration of {max_avg_duration} minutes")

if __name__ == "__main__":
    main()