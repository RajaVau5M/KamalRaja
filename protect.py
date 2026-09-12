import marshal
import zlib
import base64

filename = "5M.py"

with open(filename, "r", encoding="utf-8") as f:
    code_content = f.read()

code_obj = compile(code_content, filename, 'exec')
marshaled_code = marshal.dumps(code_obj)
compressed_code = zlib.compress(marshaled_code)
encoded_code = base64.b64encode(compressed_code)

protected_stub = f"""# ==========================================
# SECURE PROTECTED BY KAMAL 
# ==========================================
import marshal, zlib, base64
exec(marshal.loads(zlib.decompress(base64.b64decode({encoded_code!r}))))
"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(protected_stub)

print("[✓] File encrypted and locked successfully!")
