import requests

class APIWrapper:

    def __init__(self):
        self.response = None
        url = None
        self.my_request = requests

    def api_get_request(self, url):
        self.response = self.my_request.get(url)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_post_request(self, url):
        self.response = self.my_request.post(url)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_get_request_with_param(self, url,param,config):
        params_dict = self.prepair_url_params(param,config)
        url = self.add_query_Parameters_to_api_request(url, params_dict)
        self.response = self.my_request.get(url)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code


    def prepair_url_params(self, input_,config):
        params_dict = {}
        for key in input_.keys():
            params = config[key]
            if input_[key] == True:
                key = params.split("=")[0]
                val = params.split("=")[1]
                params_dict[key] = val
            else:
                params_dict[params] = input_[key]
        return params_dict


    def add_query_Parameters_to_api_request(self,url, params):
        query_params = ''.join([f"&{key}={value}" for key, value in params.items()])
        return url + query_params
