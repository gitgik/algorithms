```python
class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.createBuckets()
        
    def createBuckets(self):
        return [[] for i in range(self.size)]
    
    def set(self, key, value):
        # get bucket hash
        bucket_hash = hash(key) % self.size
        bucket = self.hash_table[bucket_hash]
        
        found_key = False
        for idx, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[idx] = (key, value)
        else:
            bucket.append((key, value))
    
    def get(self, key):
        # Get the index of the bucket holding the key using the hash function
        index = hash(key) % self.size
        
        # get the bucket using the index
        bucket = self.hash_table[index]
        
        found_key = False
        for idx, record in enumerate(bucket):
            record_key, record_val = record
            if key == record_key:
                found_key = True
                break
        return record_val if found_key else None
    
    def delete(self, key):
        bucket_hash = hash(key) % self.size
        found_key = False
        for idx, record in enumerate(self.hash_table[bucket_hash]):
            record_key, record_value = record
            if key == record_key:
                found_key = True
                break
        if found_key:
            # delete
            self.hash_table.pop(idx)
        else:
            return f"Key '{key}' does not exist"
            
        
```


```python
hashmap = HashMap(10)
```


```python
hashmap.set("something", "soweto")
for i in range(5):
    hashmap.set(f"{i}", i)
```


```python
hashmap.get("something")

```




    'soweto'




```python

```
