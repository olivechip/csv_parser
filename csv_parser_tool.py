import csv
from collections import defaultdict
import json

total_deals = 0
total_value = 0
won_deals = 0
lost_deals = 0
won_value = 0
lost_value = 0
deals_by_client = defaultdict(int)
deals_by_client_value = defaultdict(int)

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for line in csv_reader:
        print(line)
        total_deals += 1
        total_value += float(line['Deal Value'])
        
        if line['Status'] == 'Won':
            won_deals += 1
            won_value += float(line['Deal Value'])
        else:
            lost_deals += 1
            lost_value += float(line['Deal Value'])
            
        client = line['Client']
        deals_by_client[client] += 1
        deals_by_client_value[client] += float(line['Deal Value'])

# output in console
print(f"Total Deals: {total_deals}")
print(f"Total Value: {total_value}")
print(f"Average Deal Value: ${total_value/total_deals}")
print(f"Won Deals: {won_deals}")
print(f"Lost Deals: {lost_deals}")
print(f"Won Value: ${won_value}")
print(f"Lost Value: ${lost_value}")

print(f"Deals by Clients:")
for client, count in deals_by_client.items():
    print(f"{client}: {count} deals, ${deals_by_client_value[client]:,.2f}")

# converting data to JSON
stats = {
    "Total Deals": total_deals,
    "Total Value": total_value,
    "Average Deal Value": total_value/total_deals,
    "Won Deals": won_deals,
    "Lost Deals": lost_deals,
    "Won Value": won_value,
    "Lost Value": lost_value
}

client_stats = []
for client, count in deals_by_client.items():
    client_stats.append({
        "Client": client,
        "Number of Deals": count,
        "Total Deal Value": f"${deals_by_client_value[client]:,.2f}"
    })

# output in JSON
with open('stats.json', 'w') as stats_file:
    json.dump(stats, stats_file, indent=4)
    
with open('client_stats.json', 'w') as stats_file:
    json.dump(client_stats, stats_file, indent=4)