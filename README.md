# Run tests

```shell script
pytest -s --alluredir allure-results
```

# Generate and open report

```shell script
allure generate allure-results -o allure-report -c
allure open allure-report
```

or

```shell script
allure serve allure-results
```
