import json

with open("cleaned_memory_names.json", "r", encoding="utf-8") as f:
    data = json.load(f)


mem_name = input("Enter memory name: ").strip().lower()
print("------------------------------------------------")

matches = []

for pages in data:
    for page_name, page_items in pages.items(): # page is like Sunny/Memories and Effie/Memories
        for item in page_items:
            if mem_name in item["Name"].strip().lower():
                matches.append(item)
                print(page_name)
                print("-" * len(page_name))
                print("Name: " + item["Name"])
                print("Description: " + item["Description"])
                print("------------------------------------------------")

if not matches:
    print("No matches")

        # if mem_name in m.get("Name", "").lower():
        #     print("-------------------")
        #     for k,v in m.items():
        #         print(f"{k}: {v}")