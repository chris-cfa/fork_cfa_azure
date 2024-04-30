import unittest

from cfa_azure.helpers import read_config

class TestReadConfig(unittest.TestCase):
    def test_config_dict(self):
        config = read_config("./ex_config.toml")
        self.assertIsInstance(config, dict)

    def test_config_info(self):
        config = read_config("./ex_config.toml")
        expected = {'Authentication': {'subscription_id': 'sub_id', 'resource_group': 'resource_group',
                                       'user_assigned_identity': 'user_assigned_identity', 'tenant_id': 'tenant_id', 
                                       'client_id': 'client_id', 'principal_id': 'principal_id', 'application_id': 'application_id', 
                                       'vault_url': 'https://cfa-common-adf-prd.vault.azure.net/', 
                                       'vault_sp_secret_id': 'CFA-SECRET_ID', 'vault_sa_secret_id':
                                       'CFA-SA_SECRET_ID', 'vault_ab_secret_id': 'CFA-AB_SECRET_ID', 'subnet_id': 'subnet_id'}, 
                    'Batch': {'batch_account_name': 'batch_account_name', 'batch_url': 'batch_url', 'batch_service_url': 'batch_service_url', 
                              'pool-node-count': 2, 'pool_vm_size': 'STANDARD_A2_V2', 'task_threads': 16, 'task_timeout_minutes': 90}, 
                    'Storage': {'storage_account_name': 'storage_account_name', 'storage_account_url': 'storage_account_url'}, 
                    'Container': {'container_account_name': 'container_account_name', 'container_registry_url': 'container_registry_url', 
                                  'container_name': 'container_name', 'container_image_name': 'container_image_name', 
                                  'container_registry_username': 'registry_username', 'container_registry_password': 'registry_password', 
                                  'container_registry_server': 'registry_server'}}
        self.assertDictEqual(config, expected)

if __name__ == '__main__':
    unittest.main()   