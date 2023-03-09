links = [(lambda i: "http://" + i if i.endswith('.com') else "http://" + i + ".com")(i)
         for i in ['www.vk.com', 'vk.com', 'www.vk', 'asf'] if i.startswith('www')]
print (links)