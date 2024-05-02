# Determine the appropriate AWS service based on the user's requirement
def main():
    # Define the user's requirement: object_storage, serverless_computing, virtual_server, other
    user_requirement = 'serverless_computing'

    # If none of the above conditions match, set the service as 'Unknown'
    if user_requirement == 'object_storage':
        aws_service = 's3'
    elif user_requirement == 'virtual_server':
        aws_service = 'EC2'
    elif user_requirement == 'serverless_computing':
        aws_service = 'Lambda'
    else:
        aws_service = 'Unknown'
    # Print the recommended AWS service based on the user's requirement
    # Check if the service is not 'Unknown'
    if user_requirement != 'Unknown':
        print(f"The AWS service required is {aws_service}.")
    else:
        print(f"Error: The AWS service is {aws_service}.")

if __name__ == '__main__':
    main()