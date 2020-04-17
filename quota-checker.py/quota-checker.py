#/usr/bin/python
import googleapiclient.discovery

compute = googleapiclient.discovery.build('compute', 'v1')

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None

print(list_instances(compute, "panick-sandbox-bro", "us-central1-a"))