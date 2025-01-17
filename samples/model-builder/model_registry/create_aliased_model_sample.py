# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_model_registry_create_aliased_model_sample]

from google.cloud import aiplatform


def create_aliased_model_sample(
    model_id: str, version_id: str, project: str, location: str
):
    """
    Initialize a Model resource to represent an existing model version with custom alias.
    Args:
        model_id: The ID of the model to initialize. Parent resource name of the model is also accepted.
        version_id: The version ID or version alias of the model to initialize.
        project: The project.
        location: The location.
    Returns:
        Model resource.
    """
    # Initialize the client.
    aiplatform.init(project=project, location=location)

    # Initialize the Model resource with the ID 'model_id'. The version can be also provided using @ annotation in
    # the parent resource name:
    # 'projects/<your-project-id>/locations/<your-region>/models/<your-model-id>@<your-version-id>'.

    aliased_model = aiplatform.Model(model_name=model_id, version=version_id)

    return aliased_model


# [END aiplatform_model_registry_create_aliased_model_sample]
