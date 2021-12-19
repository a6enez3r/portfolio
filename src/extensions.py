"""
    extensions.py: init flask extensions
"""
import secure

csp = secure.ContentSecurityPolicy()
hsts = secure.StrictTransportSecurity()
xfo = secure.XFrameOptions().deny()
referrer = secure.ReferrerPolicy().strict_origin()
cache = secure.CacheControl().no_cache()
secure_headers = secure.Secure(
    csp=csp, hsts=hsts, xfo=xfo, referrer=referrer, cache=cache
)
