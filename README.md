## Rate Limiters [In progress]
Implementation of Rate Limiters

# Algorithms implemented
* Token Bucket

# Token Bucket Algorithm
A token bucket is a container with pre-defined capacity. Tokens are put in the bucket periodically. Once the bucket is full, no more tokens are added.
* If there are enough tokens, it will be used as credit for each request, and the request goes through.
* If there are not enough tokens, the request is dropped.