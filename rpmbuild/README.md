Drop the latest NewRelic licensed ZIP into the SOURCES directory and run the command:

```
rpmbuild -bb --clean -D "version 3.12.0" SPECS/newrelic-java.spec
```

Substituting the version as needed.