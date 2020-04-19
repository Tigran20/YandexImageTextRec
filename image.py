import base64
import json
import os


def encode_file(file):
    with open(file, 'rb') as f:
        file_content = f.read()
    return base64.b64encode(file_content).decode('utf-8')


outfile = encode_file('bla.jpeg')  # my image file

out = {
    "folderId": "b1gah3b0s98i5term047",
    "analyze_specs": [{
        "content": outfile,
        "features": [{
            "type": "TEXT_DETECTION",
            "text_detection_config": {
                "language_codes": ["*"]
            }
        }]
    }],
}

# make request
with open('body.json', 'w') as f:
    json.dump(out, f)

# REAL IAM_TOKEN is REQUARED
os.system(
    "export IAM_TOKEN=CggVAgAAABoBMxKABLzSzia0PpLpR8Ll149B5T5J14N-BqLnUNUzt8ANJg7ZLW5TW6363UouDsTHAT3wirqHvf_EBZ5shSPO-E0TKa6Ef0pqx2w-EPgAYO-xqfT1IKgo-OLS1VSgL-8Qqh1zcMbtQdGLmDP0kQ_MdQTbN5ueFCyQ0bEZVu6VMBUQxzF6ItAa0MRLBxDWEdnD6FcEjJueIfrmU0B3s-d3jfKTVzySENGCLpY6mVitDbfgsL6fo558oMUS6GALM1TX5ZG5qkYwBKApjBdLy7fdwZBqql6FNrmC1U9RLpr73NOpdPCmDWb_rVOvPnj1d9sC3t9fY7OYd4DMDclR0gOQPKFY64CFHgrVx7308N-iSf42K3Gy5mRLB5PDTZ75KDDI17cJQsAsABu86p9FzCaHlNx0ZGcH1w2-oWnzrvMWLo3XUP1Od9Qaao6_xthmDBcS6_5A-qV-zAneGLwWTvJLuRmjP10s4JnA4klr9IovasQHY9elsT2sQBBgBCX4fSsSJ4jtxgbrUFsF-2kJXq-W0jEfSkJPQq00tSpUg16ei8rK4ukK4b5OrO9OFJqfPwEUB-WYpxj3LWo-Kj8j8L4nPVdct3sH6LLlcVre-NksxZklsdiO2Dz2icTTQvAjiKJWotbQvIoWXLq8s_jcgVjf7x94SqyVaMynzD2I-nngg8XIeNNmGiQQ89bx9AUYs6j09AUiFgoUYWplbWl0MG1wMjZybzNsZDh2a2s=")
os.system(
    "curl -X POST -H \"Content-Type: application/json\" -H \"Authorization: Bearer CggVAgAAABoBMxKABLzSzia0PpLpR8Ll149B5T5J14N-BqLnUNUzt8ANJg7ZLW5TW6363UouDsTHAT3wirqHvf_EBZ5shSPO-E0TKa6Ef0pqx2w-EPgAYO-xqfT1IKgo-OLS1VSgL-8Qqh1zcMbtQdGLmDP0kQ_MdQTbN5ueFCyQ0bEZVu6VMBUQxzF6ItAa0MRLBxDWEdnD6FcEjJueIfrmU0B3s-d3jfKTVzySENGCLpY6mVitDbfgsL6fo558oMUS6GALM1TX5ZG5qkYwBKApjBdLy7fdwZBqql6FNrmC1U9RLpr73NOpdPCmDWb_rVOvPnj1d9sC3t9fY7OYd4DMDclR0gOQPKFY64CFHgrVx7308N-iSf42K3Gy5mRLB5PDTZ75KDDI17cJQsAsABu86p9FzCaHlNx0ZGcH1w2-oWnzrvMWLo3XUP1Od9Qaao6_xthmDBcS6_5A-qV-zAneGLwWTvJLuRmjP10s4JnA4klr9IovasQHY9elsT2sQBBgBCX4fSsSJ4jtxgbrUFsF-2kJXq-W0jEfSkJPQq00tSpUg16ei8rK4ukK4b5OrO9OFJqfPwEUB-WYpxj3LWo-Kj8j8L4nPVdct3sH6LLlcVre-NksxZklsdiO2Dz2icTTQvAjiKJWotbQvIoWXLq8s_jcgVjf7x94SqyVaMynzD2I-nngg8XIeNNmGiQQ89bx9AUYs6j09AUiFgoUYWplbWl0MG1wMjZybzNsZDh2a2s=\" -d @body.json https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze > output.json")

# YandexVisions answer in output.json