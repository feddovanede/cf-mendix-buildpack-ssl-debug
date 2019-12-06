import os
import json
import start
from m2ee import M2EE
from m2ee.config import M2EEConfig


class TestCaseAzureBlobStoreDryRun:

    azure_storage_vcap_example = """
{
        "objectstore": [
   {
    "binding_name": null,
    "credentials": {
     "account_name": "sapcp4f4f4f4f4f4f4f4f4f4f",
     "container_name": "sapcp-osaas-2d2d2d2d-cccc-4444-8888-4ed76dca688e",
     "container_uri": "https://sapcp4f81hh2hps11tx7iuc7.blob.core.windows.net/sapcp-osaas-2d2d2d2d-cccc-4444-8888-4ed76dca688e",
     "region": "westeurope",
     "sas_token": "sig=JC1hALu1%2FOFA%1FzyuCzuZKivlb%1IIYktBYxHKPF2OJz3U%3D\u0026sv=2017-01-17\u0026spr=https\u0026si=77777777-ffff-4444-bbbb-bdeafdd87d00\u0026sr=c"
    },
    "instance_name": "test-azure-nl_Test_XgXgX",
    "label": "objectstore",
    "name": "test-azure-nl_Test_XgXgX",
    "plan": "azure-standard",
    "provider": null,
    "syslog_drain_url": null,
    "tags": [
     "blobStore",
     "objectStore"
    ],
    "volume_mounts": []
   }
  ]
}
    """  # noqa

    def test_azure_blob_store(self):
        vcap = json.loads(self.azure_storage_vcap_example)
        os.environ["MENDIX_BLOBSTORE_TYPE"] = "azure"
        m2ee = M2EE.__new__(M2EE)
        m2ee.config = M2EEConfig()
        config = start._get_azure_storage_specific_config(vcap, m2ee)
        assert config["com.mendix.storage.azure.Container"] == "mendix"
        assert (
            config["com.mendix.storage.azure.SharedAccessSignature"]
            == "sig=JC1hALu1%2FOFA%1FzyuCzuZKivlb%1IIYktBYxHKPF2OJz3U%3D\u0026sv=2017-01-17\u0026spr=https\u0026si=77777777-ffff-4444-bbbb-bdeafdd87d00\u0026sr=c"  # noqa
        )
