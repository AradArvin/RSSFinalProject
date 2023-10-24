

JWT API Reference
-----------------
**A JSON web token(JWT)** is JSON Object which is used to securely transfer information over the web(between two parties). 
It can be used for an authentication system and can also be used for information exchange.The token is mainly composed of 
header, payload, signature. These three parts are separated by dots(.). JWT defines the structure of information we are 
sending from one party to the another, and it comes in two forms – Serialized, Deserialized. The Serialized approach is 
mainly used to transfer the data through the network with each request and response. While the deserialized approach is 
used to read and write data to the web token.

A *header* in a JWT is mostly used to describe the cryptographic operations applied to the JWT like signing/decryption 
technique used on it. It can also contain the data about the media/content type of the information we are sending.This 
information is present as a JSON object then this JSON object is encoded to BASE64URL. The cryptographic operations in 
the header define whether the JWT is signed/unsigned or encrypted and are so then what algorithm techniques to use.

**The authentication will be implanted using JWT**