""" Providers Resource


"""

import os
from flask import request
from flask_restful import Resource
from data_resource_api.api import VersionedResource
from data_resource_api.api.v1_0_0 import V1_0_0_ProvidersHandler
from data_resource_api.auth import login_required


class ProvidersResource(VersionedResource):
    def get_request_handler(self, headers):
        api_version = self.get_api_version(headers)
        if api_version == '1.0.0':
            request_handler = V1_0_0_ProvidersHandler()
        else:
            request_handler = V1_0_0_ProvidersHandler()
        return request_handler

    @login_required
    def get(self):
        return self.get_request_handler(request.headers).get_all_providers()

    @login_required
    def post(self):
        return self.get_request_handler(request.headers).add_new_provider(
            request.get_json())


class ProviderResource(ProvidersResource):
    @login_required
    def get(self, id):
        return self.get_request_handler(request.headers).get_provider_by_id(id)

    @login_required
    def put(self, id):
        return self.get_request_handler(request.headers).update_provider(
            request.get_json(), id)

    @login_required
    def delete(self, id):
        return self.get_request_handler(request.headers).delete_provider_by_id(
            id)


class ProviderProgramResource(ProviderResource):
    @login_required
    def get(self, id):
        return self.get_request_handler(
            request.headers).get_programs_by_provider(id)
