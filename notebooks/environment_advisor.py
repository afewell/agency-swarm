# Sample mock data representing environmental issues for different regions
data_by_region = {
    'North America': {
        'issues': ['High carbon emissions from vehicles', 'Excessive water usage'],
        'actions': ['Use public transportation or carpool', 'Install low-flow showerheads and faucets']
    },
    'Europe': {
        'issues': ['Air pollution in urban areas', 'Overuse of single-use plastics'],
        'actions': ['Support clean air initiatives', 'Use reusable bags and containers']
    },
    'Asia': {
        'issues': ['Deforestation', 'High levels of air and water pollution'],
        'actions': ['Support reforestation projects', 'Avoid products that contribute to pollution']
    }
}

# Function to provide advice based on the user's region

def get_advice_by_region(region):
    region_data = data_by_region.get(region)
    if not region_data:
        return 'No data available for this region.'
    advice = '\n'.join([
        '* ' + action for action in region_data['actions']
    ])
    return advice

# User interactive interface

def main():
    print('Welcome to the Environmental Impact Advisor.')
    print('Please enter your region (North America, Europe, Asia):')
    user_region = input()
    advice = get_advice_by_region(user_region)
    print('\nThe environmental issues in your region:')
    for issue in data_by_region[user_region]['issues']:
        print(f' - {issue}')
    print('\nHere are some actions you can take to reduce your carbon footprint:')
    print(advice)

# Run the interactive tool
if __name__ == '__main__':
    main()
