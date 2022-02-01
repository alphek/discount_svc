import hashlib


def generate_codes(brand_id, campaign_id, count):
    # to prevent anyone else generate a valid code, to further safety brand secret key can be used  to hash as well
    # code is currently too long must be changed with something more useful and shorter
    codes = []
    for i in range(0, count):
        code_str = str(brand_id) + str(campaign_id) + str(i)
        codes.append(int(hashlib.sha256(code_str.encode('utf-8')).hexdigest(), 16))
    return codes
