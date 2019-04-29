
######################################################################
########################## PARAMETERS ################################
BREED = "hound"
SUB_BREED = "afghan"

endpoints = {
            "breeds": "breeds/list/all",
            "breeds_random_image": "breeds/image/random",   
            "breeds_multi_images": "breeds/image/random/{0}",          
            "sub_breeds": "breed/{0}/list",
            "sub_images": "breed/{0}/{1}/images",
            "sub_random_image": "breed/{0}/{1}/images/random",
            "sub_multi_images": "breed/{0}/{1}/images/random/{2}",
            "breed_images": "breed/{0}/images",
            "breed_random_image": "breed/{0}/images/random",
            "breed_multi_images": "breed/{0}/images/random/{1}"
            }

class Endpoint:
    def __init__(self):
        pass

    def get_all_list(self):
        ep = list()
        ep.append(self.breed_images())
        ep.append(self.breed_multi_images())
        ep.append(self.breed_random_image())
        ep.append(self.breeds())
        ep.append(self.breeds_random_image())
        ep.append(self.breeds_multi_images())
        ep.append(self.sub_breeds())
        ep.append(self.sub_images())
        ep.append(self.sub_multi_images())
        ep.append(self.sub_random_image())
        return ep 

    def get_random_endpoints(self):
        ep = list()
        ep.append(self.breed_random_image())
        ep.append(self.breeds_random_image())
        ep.append(self.sub_random_image())
        return ep

    def get_multi_endpoints(self):
        ep = list()
        ep.append(self.breed_multi_images())
        ep.append(self.breeds_multi_images())
        ep.append(self.sub_multi_images())
        return ep

    def get_all_dict(self):
        ep = dict()
        ep["breeds"] = self.breeds()
        ep["breeds_random_image"] = self.breeds_random_image()
        ep["breeds_multi_images"] = self.breeds_multi_images()
        #######
        ep["breed_images"] = self.breed_images()
        ep["breed_multi_images"] = self.breed_multi_images()
        ep["breed_random_image"] = self.breed_random_image()
        #######
        ep["sub_breeds"] = self.sub_breeds()
        ep["sub_images"] = self.sub_images()
        ep["sub_multi_images"] = self.sub_multi_images()
        ep["sub_random_image"] = self.sub_random_image()
        return ep 


    def breeds(self):
        return endpoints["breeds"]

    def breeds_random_image(self):
        return endpoints["breeds_random_image"]

    def breeds_multi_images(self, count = 3):
        return endpoints["breeds_multi_images"].format(count)

    def breed_images(self, breed = BREED):
        return endpoints["breed_images"].format(breed)

    def breed_random_image(self, breed = BREED):
        return endpoints["breed_random_image"].format(breed)

    def breed_multi_images(self, breed = BREED, count = 3):
        return endpoints["breed_multi_images"].format(breed, count)

    def sub_breeds(self, breed = BREED):
        return endpoints["sub_breeds"].format(breed)
    
    def sub_images(self, breed = BREED, sub_breed = SUB_BREED):
        return endpoints["sub_images"].format(breed, sub_breed)

    def sub_random_image(self, breed = BREED, sub_breed = SUB_BREED):
        return endpoints["sub_random_image"].format(breed, sub_breed)

    def sub_multi_images(self, breed = BREED, sub_breed = SUB_BREED, count = 3):
        return endpoints["sub_multi_images"].format(breed, sub_breed, count)


