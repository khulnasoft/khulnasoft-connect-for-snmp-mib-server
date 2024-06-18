# README

Khulnasoft Connect for SNMP MIB Server is an open source packaged component for of Khulnasoft Connect for SNMP.
This project contains a community collection of SNMP MIBs.

## Purpose

This project is a repository of MIBS packaged as a OCI compliant container for use with Khulnasoft Connect for SNMP


## Usage

This project is only intended to be used as part of a Khulnasoft Connect for SNMP Deployment

## Support

Khulnasoft Connect for SNMP is an open source product developed by Khulnasofters with contributions from the community of partners and customers. This unique product will be enhanced, maintained and supported by the community, led by Khulnasofters with deep subject matter expertise. The primary reason why Khulnasoft is taking this approach is to push product development closer to those that use and depend upon it. This direct connection will help us all be more successful and move at a rapid pace.

Post a question to Khulnasoft Answers using the tag "Khulnasoft Connect For SNMP"

Join the #khulnasoft-connect-for-snmp room in the khulnasoft-usergroups Slack Workspace. If you don't yet have an account [sign up](https://docs.khulnasoft.com/Documentation/Community/1.0/community/Chat)

Please use the GitHub issue tracker to submit bugs or request enhancements: https://github.com/khulnasoft/khulnasoft-connect-for-snmp-mib-server/issues

Get involved, try it out, ask questions, contribute filters, and make new friends!

## Contributing

We welcome feedback and contributions from the community! Please see our [contribution guidelines](CONTRIBUTING.md) for more information on how to get involved.

## License

* Individual MIBs licensed as indicated

* NGNIX [BSD-2-Clause](https://hub.docker.com/_/nginx/)



## Development Instructions for Mib Server

> This is used as a reference steps while working on development aspects of SNMP Mib Server component of Khulnasoft Connect for SNMP!

#### Get Started
```
git clone git@github.com:khulnasoft/khulnasoft-connect-for-snmp-mib-server.git
cd "khulnasoft-connect-for-snmp-mib-server"
```

#### Run MongoDB

```docker run -d -p 27017:27017 -v ./data:/data/db mongo```

#### Setup Environment for Mib Server
```
export MONGO_SERVICE_SERVICE_HOST=<mongo_host>
export MONGO_SERVICE_SERVICE_PORT=<mongo_port>
export MIBS_FILES_URL=http://0.0.0.0:5000/files/asn1/@mib@
```
#### Install Poetry
```pip3 install poetry```

#### Run Mib Server
```
poetry install
poetry run kc4snmp-mib-server
```