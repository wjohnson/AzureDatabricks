# Databricks Job Linter

A sample set of classes to read in a Databricks Job json and confirm that it follows a set of plaintext rules.

## Example Rules

A rule is made up of a dot notation path for the json, a colon(:), and the expected value.

```
path.to.element: value
```

Here are some example values and illustration of the special values: `?`, `[?]`, and `[..., *]` values.

* **["a","b",*]** means **Array must contain a and b but additional values allowed**
* **?** means **User Input Required**
* **[?]** means **User Input Required for an Array**
* **[]** means **Literal Empty Array**
* **300** means **Literal 300**
* **true** means **Literal True**
* **(an empty string)** means **string field should be empty**

Some limited samples
```
notebook_task.notebook_path: ? # Requires a value in notebook_task.notebook_path
new_cluster.custom_tags: [?] # Requires new_cluster.custom_tags to have a populated array
email_notifications.on_start: [] # Requires email_notification.on_start to be an empty array
timeout_seconds: 300 # Requires timeout_seconds to be 300
retry_on_timeout: true # Requires retry_on_timeout to be True
```

## Example Usage

One that fails:
```
python .\src\driver.py .\samples\batch-driver-only.json .\samples\batch-driver-def.txt

# RETURNS:
# Validation Failed:
# ExactMatch: new_cluster.num_workers should be 0
```
