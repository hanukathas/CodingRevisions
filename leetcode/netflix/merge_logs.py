def merge_logs(logs:list):
    logs.sort(key=lambda items: items["timestamp"])




if __name__ == '__main__':
    logs1 = [{"message":"Server A started","timestamp":"2023-01-01 10:00:00"},{"message":"Server B started","timestamp":"2023-01-01 10:02:00"},{"message":"Server C started","timestamp":"2023-01-01 10:01:00"}]
    print(merge_logs(logs1))
    logs2 = [{"message":"Error in Server B","timestamp":"2023-01-01 15:30:00"},{"message":"Warning in Server A","timestamp":"2023-01-01 15:29:59"},{"message":"Server C shutdown","timestamp":"2023-01-01 15:30:01"}]
    print(merge_logs(logs2))