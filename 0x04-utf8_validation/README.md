# UTF-8 validation and encoding

|  Byte 1  |  Byte 2  |  Byte 3  |  Byte 4  |
|    --    |    --    |    --    |    --    |
| 0xxxxxxx |          |          |          | 
| 110xxxxx | 10xxxxxx |          |          |
| 1110xxxx | 10xxxxxx | 10xxxxxx |          |
| 11110xxx | 10xxxxxx | 10xxxxxx | 10xxxxxx |
