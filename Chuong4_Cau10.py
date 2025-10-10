from time import sleep

# Hình 1: tam giác vuông
hinh1 = """
      *
      * *
      * * *
* * * * * * *
* * * 
* *
*
"""

# Hình 2: hình chữ nhật
hinh2 = """
      *
      * *
      *   *
* * * * * * *
*   * 
* *
*
"""

# Hình 3: hình tam giác cân
hinh3 = """
      * * * * 
      * * *
      * *
      *
    * *
  * * * 
* * * *
        
"""

# Hình 4: hình thoi
hinh4 = """
      * * * * 
      *   *
      * *
      *
    * *
  *   * 
* * * *
"""

# In lần lượt từng hình, mỗi hình cách nhau 5 giây
for i, h in enumerate([hinh1, hinh2, hinh3, hinh4], start=1):
    print(f"Hình {i}:\n{h}")
    sleep(5)
