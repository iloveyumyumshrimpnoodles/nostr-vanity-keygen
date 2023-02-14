"""
This project is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this code. 
If not, see <https://www.gnu.org/licenses/>. 
"""

import sys

from nostr.key import PrivateKey

if len(sys.argv) == 1:
    sys.exit(f"usage: python3 {sys.argv[0]} your preferred keyword")

prefix = " ".join(sys.argv[1:])
possible_chars = "023456789acdefghjklmnpqrstuvwxy"

if max([not i in possible_chars for i in prefix]):
    print("Illegal keyword detected!")
    exit()

def gen():
    private_key = PrivateKey()
    public_key = private_key.public_key

    return private_key.bech32(), public_key.bech32()

k = gen()
i = 0
while not k[1].startswith(prefix) or not k[1].endswith(prefix):
    try:
        k = gen()
        i += 1

        print(f"[:{i+1}:] Generated -> {k[0]}:{k[1]}")
    
    except:
        break

if k[1].startswith(prefix) or k[1].endswith(prefix):
    print(f"\n\nBingo ==> {k[0]}:{k[1]}")
else:
    print(f"\n\nFailed.")

print(f"Tries: {i+1}")