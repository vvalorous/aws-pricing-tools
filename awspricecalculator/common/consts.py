import os, logging

# COMMON
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
AWS_PRICE_CALCULATOR_VERSION = "v2.0"

LOG_LEVEL = os.environ.get('LOG_LEVEL',logging.INFO)
DEFAULT_CURRENCY = "USD"
FORECAST_PERIOD_MONTHLY = "monthly"
FORECAST_PERIOD_YEARLY = "yearly"

HOURS_IN_MONTH = 720

SERVICE_CODE_AWS_DATA_TRANSFER = 'AWSDataTransfer'

REGION_MAP = {'us-east-1':'US East (N. Virginia)',
              'us-east-2':'US East (Ohio)',
              'us-west-1':'US West (N. California)',
              'us-west-2':'US West (Oregon)',
              'ca-central-1':'Canada (Central)',
              'eu-west-1':'EU (Ireland)',
              'eu-west-2':'EU (London)',
              'eu-west-3':'EU (Paris)',
              'eu-central-1':'EU (Frankfurt)',
              'ap-northeast-1':'Asia Pacific (Tokyo)',
              'ap-northeast-2':'Asia Pacific (Seoul)',
              'ap-southeast-1':'Asia Pacific (Singapore)',
              'ap-southeast-2':'Asia Pacific (Sydney)',
              'sa-east-1':'South America (Sao Paulo)',
              'ap-south-1':'Asia Pacific (Mumbai)',
              'cn-northwest-1':'China (Ningxia)'
              }

#TODO: update for China and Paris regions
REGION_PREFIX_MAP = {'us-east-1':'',
              'us-east-2':'USE2-',
              'us-west-1':'USW1-',
              'us-west-2':'USW2-',
              'ca-central-1':'CAN1-',
              'eu-west-1':'EU-',
              'eu-west-2':'EUW2-',
              'eu-west-3':'EUW3',
              'eu-central-1':'EUC1-',
              'ap-northeast-1':'APN1-',
              'ap-northeast-2':'APN2-',
              'ap-southeast-1':'APS1-',
              'ap-southeast-2':'APS2-',
              'sa-east-1':'SAE1-',
              'ap-south-1':'APS3-',
              'cn-northwest-1':'',
              'US East (N. Virginia)':'',
              'US East (Ohio)':'USE2-',
              'US West (N. California)':'USW1-',
              'US West (Oregon)':'USW2-',
              'Canada (Central)':'CAN1-',
              'EU (Ireland)':'EU-',
              'EU (London)':'EUW2-',
              'EU (Frankfurt)':'EUC1-',
              'Asia Pacific (Tokyo)':'APN1-',
              'Asia Pacific (Seoul)':'APN2-',
              'Asia Pacific (Singapore)':'APS1-',
              'Asia Pacific (Sydney)':'APS2-',
              'South America (Sao Paulo)':'SAE1-',
              'Asia Pacific (Mumbai)':'APS3-',
              'AWS GovCloud (US)':'UGW1-',
              'External':'',
              'Any': ''
              }



REGION_REPORT_MAP = {'us-east-1':'N. Virginia',
              'us-east-2':'Ohio',
              'us-west-1':'N. California',
              'us-west-2':'Oregon',
              'ca-central-1':'Canada',
              'eu-west-1':'Ireland',
              'eu-west-2':'London',
              'eu-central-1':'Frankfurt',
              'ap-northeast-1':'Tokyo',
              'ap-northeast-2':'Seoul',
              'ap-southeast-1':'Singapore',
              'ap-southeast-2':'Sydney',
              'sa-east-1':'Sao Paulo',
              'ap-south-1':'Mumbai',
              'cn-northwest-1':'Ningxia',
              'eu-west-3':'Paris'
              }



SERVICE_EC2 = 'ec2'
SERVICE_ELB = 'elb'
SERVICE_EBS = 'ebs'
SERVICE_S3 = 's3'
SERVICE_RDS = 'rds'
SERVICE_LAMBDA = 'lambda'
SERVICE_DYNAMODB= 'dynamodb'
SERVICE_KINESIS = 'kinesis'
SERVICE_ALL = 'all'

NOT_APPLICABLE = 'NA'


SUPPORTED_SERVICES = (SERVICE_S3, SERVICE_EC2, SERVICE_RDS, SERVICE_LAMBDA, SERVICE_DYNAMODB, SERVICE_KINESIS)

SUPPORTED_REGIONS = ('us-east-1','us-east-2', 'us-west-1', 'us-west-2','ca-central-1', 'eu-west-1','eu-west-2',
                     'eu-central-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2',
                     'sa-east-1','ap-south-1','cn-northwest-1', 'eu-west-3'
                     )

SUPPORTED_INSTANCE_TYPES = ('t1.micro' , 't2.nano' , 't2.micro' , 't2.small' , 't2.medium' , 't2.large', 't2.xlarge', 't2.2xlarge', 'm1.small',
                            'm1.medium' , 'm1.large' , 'm1.xlarge' , 'm3.medium' , 'm3.large' , 'm3.xlarge' , 'm3.2xlarge',
                            'm4.large' , 'm4.xlarge' , 'm4.2xlarge' , 'm4.4xlarge' , 'm4.10xlarge' , 'm2.xlarge',
                            'm5.large' , 'm5.xlarge' , 'm5.2xlarge' , 'm5.4xlarge' , 'm5.12xlarge' , 'm5.24xlarge',
                            'm2.2xlarge' , 'm2.4xlarge' , 'cr1.8xlarge' ,'r4.large', 'r4.xlarge', 'r4.2xlarge', 'r4.4xlarge', 'r4.8xlarge',
                            'r4.16xlarge' 'r3.large' , 'r3.xlarge' , 'r3.2xlarge',
                            'r3.4xlarge' , 'r3.8xlarge' , 'x1.4xlarge' , 'x1.8xlarge' , 'x1.16xlarge' , 'x1.32xlarge',
                            'i2.xlarge' , 'i2.2xlarge' , 'i2.4xlarge' , 'i2.8xlarge',
                            'i3.large', 'i3.xlarge', 'i3.2xlarge', 'i3.4xlarge', 'i3.8xlarge',
                            'hi1.4xlarge' , 'hs1.8xlarge',
                            'c1.medium' , 'c1.xlarge' , 'c3.large' , 'c3.xlarge' , 'c3.2xlarge' , 'c3.4xlarge',
                            'c3.8xlarge' , 'c4.large' , 'c4.xlarge' , 'c4.2xlarge' , 'c4.4xlarge' , 'c4.8xlarge',
                            'c5.large' , 'c5.xlarge' , 'c5.2xlarge' , 'c5.4xlarge' , 'c5.9xlarge' , 'c5.18xlarge',
                            'cc1.4xlarge' , 'cc2.8xlarge' , 'g2.2xlarge' , 'g2.8xlarge' , 'cg1.4xlarge' , 'd2.xlarge',
                            'd2.2xlarge' , 'd2.4xlarge' , 'd2.8xlarge')

SERVICE_INDEX_MAP = {SERVICE_S3:'AmazonS3', SERVICE_EC2:'AmazonEC2', SERVICE_RDS:'AmazonRDS',
                     SERVICE_LAMBDA:'AWSLambda', SERVICE_DYNAMODB:'AmazonDynamoDB', SERVICE_KINESIS:'AmazonKinesis'}


SCRIPT_TERM_TYPE_ON_DEMAND = 'on-demand'
SCRIPT_TERM_TYPE_RESERVED = 'reserved'

TERM_TYPE_RESERVED = 'Reserved'
TERM_TYPE_ON_DEMAND = 'OnDemand'

SUPPORTED_TERM_TYPES = (SCRIPT_TERM_TYPE_ON_DEMAND, SCRIPT_TERM_TYPE_RESERVED)


TERM_TYPE_MAP = {SCRIPT_TERM_TYPE_ON_DEMAND:'OnDemand', SCRIPT_TERM_TYPE_RESERVED:'Reserved'}


PRODUCT_FAMILY_COMPUTE_INSTANCE = 'Compute Instance'
PRODUCT_FAMILY_DATABASE_INSTANCE = 'Database Instance'
PRODUCT_FAMILY_DATA_TRANSFER = 'Data Transfer'
PRODUCT_FAMILY_FEE = 'Fee'
PRODUCT_FAMILY_API_REQUEST = 'API Request'
PRODUCT_FAMILY_STORAGE = 'Storage'
PRODUCT_FAMILY_SYSTEM_OPERATION = 'System Operation'
PRODUCT_FAMILY_LOAD_BALANCER = 'Load Balancer'
PRODUCT_FAMILY_SNAPSHOT = "Storage Snapshot"
PRODUCT_FAMILY_SERVERLESS = "Serverless"
PRODUCT_FAMILY_DB_STORAGE = "Database Storage"
PRODUCT_FAMILY_DB_PIOPS = "Provisioned IOPS"
PRODUCT_FAMILY_KINESIS_STREAMS = "Kinesis Streams"



SUPPORTED_PRODUCT_FAMILIES = (PRODUCT_FAMILY_COMPUTE_INSTANCE, PRODUCT_FAMILY_DATABASE_INSTANCE,
                              PRODUCT_FAMILY_DATA_TRANSFER,PRODUCT_FAMILY_FEE, PRODUCT_FAMILY_API_REQUEST,
                              PRODUCT_FAMILY_STORAGE, PRODUCT_FAMILY_SYSTEM_OPERATION, PRODUCT_FAMILY_LOAD_BALANCER,
                              PRODUCT_FAMILY_SNAPSHOT,PRODUCT_FAMILY_SERVERLESS,PRODUCT_FAMILY_DB_STORAGE,
                              PRODUCT_FAMILY_DB_PIOPS,PRODUCT_FAMILY_KINESIS_STREAMS)



INFINITY = 'Inf'

SORT_CRITERIA_REGION = 'region'
SORT_CRITERIA_EC2_INSTANCE_TYPE = 'instance-type'
SORT_CRITERIA_OS = 'os'
SORT_CRITERIA_DB_INSTANCE_CLASS = 'db-instance-class'
SORT_CRITERIA_DB_ENGINE = 'engine'
SORT_CRITERIA_S3_STORAGE_CLASS = 'storage-class'
SORT_CRITERIA_S3_STORAGE_SIZE_GB = 'storage-size-gb'
SORT_CRITERIA_S3_DATA_RETRIEVAL_GB = 'data-retrieval-gb'
SORT_CRITERIA_S3_STORAGE_CLASS_DATA_RETRIEVAL_GB = 'storage-class-data-retrieval-gb'
SORT_CRITERIA_TO_REGION = 'to-region'
SORT_CRITERIA_LAMBDA_MEMORY = 'memory'
SORT_CRITERIA_TERM_TYPE = 'term-type'


SORT_CRITERIA_VALUE_SEPARATOR = ','

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
#EC2
EC2_OPERATING_SYSTEM_LINUX = 'Linux'
EC2_OPERATING_SYSTEM_BYOL = 'Windows BYOL'
EC2_OPERATING_SYSTEM_WINDOWS = 'Windows'
EC2_OPERATING_SYSTEM_SUSE = 'Suse'
#EC2_OPERATING_SYSTEM_SQL_WEB = 'SQL Web'
EC2_OPERATING_SYSTEM_RHEL = 'RHEL'

SCRIPT_EC2_TENANCY_SHARED = 'shared'
SCRIPT_EC2_TENANCY_DEDICATED = 'dedicated'

EC2_TENANCY_SHARED = 'Shared'
EC2_TENANCY_DEDICATED = 'Dedicated'

EC2_TENANCY_MAP = {SCRIPT_EC2_TENANCY_SHARED:EC2_TENANCY_SHARED, SCRIPT_EC2_TENANCY_DEDICATED:EC2_TENANCY_DEDICATED}


STORAGE_MEDIA_SSD = "SSD-backed"
STORAGE_MEDIA_HDD = "HDD-backed"
STORAGE_MEDIA_S3 = "AmazonS3"

EBS_VOLUME_TYPE_MAGNETIC = "Magnetic"
EBS_VOLUME_TYPE_GENERAL_PURPOSE = "General Purpose"
EBS_VOLUME_TYPE_PIOPS = "Provisioned IOPS"
EBS_VOLUME_TYPE_THROUGHPUT_OPTIMIZED = "Throughput Optimized HDD"
EBS_VOLUME_TYPE_COLD_HDD = "Cold HDD"

#Values that are valid in the calling script (which could be a Lambda function or any Python module)

#OS
SCRIPT_OPERATING_SYSTEM_LINUX = 'linux'
SCRIPT_OPERATING_SYSTEM_WINDOWS_BYOL = 'windowsbyol'
SCRIPT_OPERATING_SYSTEM_WINDOWS = 'windows'
SCRIPT_OPERATING_SYSTEM_SUSE = 'suse'
#SCRIPT_OPERATING_SYSTEM_SQL_WEB = 'sqlweb'
SCRIPT_OPERATING_SYSTEM_RHEL = 'rhel'

#License Model
SCRIPT_EC2_LICENSE_MODEL_BYOL = 'byol'
SCRIPT_EC2_LICENSE_MODEL_INCLUDED = 'included'
SCRIPT_EC2_LICENSE_MODEL_NONE_REQUIRED = 'none-required'

#EBS
SCRIPT_EBS_VOLUME_TYPE_STANDARD = 'standard'
SCRIPT_EBS_VOLUME_TYPE_IO1 = 'io1'
SCRIPT_EBS_VOLUME_TYPE_GP2 = 'gp2'
SCRIPT_EBS_VOLUME_TYPE_SC1 = 'sc1'
SCRIPT_EBS_VOLUME_TYPE_ST1 = 'st1'


#Reserved Instances
SCRIPT_EC2_OFFERING_CLASS_STANDARD = 'standard'
SCRIPT_EC2_OFFERING_CLASS_CONVERTIBLE = 'convertible'

EC2_OFFERING_CLASS_STANDARD = 'standard'
EC2_OFFERING_CLASS_CONVERTIBLE = 'convertible'

SUPPORTED_EC2_OFFERING_CLASSES = (SCRIPT_EC2_OFFERING_CLASS_STANDARD, SCRIPT_EC2_OFFERING_CLASS_CONVERTIBLE)

EC2_OFFERING_CLASS_MAP = {SCRIPT_EC2_OFFERING_CLASS_STANDARD:EC2_OFFERING_CLASS_STANDARD,
                          SCRIPT_EC2_OFFERING_CLASS_CONVERTIBLE: EC2_OFFERING_CLASS_CONVERTIBLE}



SCRIPT_EC2_PURCHASE_OPTION_PARTIAL_UPFRONT = 'partial-upfront'
SCRIPT_EC2_PURCHASE_OPTION_ALL_UPFRONT = 'all-upfront'
SCRIPT_EC2_PURCHASE_OPTION_NO_UPFRONT = 'no-upfront'

EC2_PURCHASE_OPTION_PARTIAL_UPFRONT = 'Partial Upfront'
EC2_PURCHASE_OPTION_ALL_UPFRONT = 'All Upfront'
EC2_PURCHASE_OPTION_NO_UPFRONT = 'No Upfront'

SCRIPT_EC2_RESERVED_YEARS_1 = '1'
SCRIPT_EC2_RESERVED_YEARS_3 = '3'

EC2_SUPPORTED_RESERVED_YEARS = (SCRIPT_EC2_RESERVED_YEARS_1, SCRIPT_EC2_RESERVED_YEARS_3)

EC2_RESERVED_YEAR_MAP = {SCRIPT_EC2_RESERVED_YEARS_1:'1yr', SCRIPT_EC2_RESERVED_YEARS_3:'3yr'}

EC2_SUPPORTED_PURCHASE_OPTIONS = (SCRIPT_EC2_PURCHASE_OPTION_ALL_UPFRONT, SCRIPT_EC2_PURCHASE_OPTION_NO_UPFRONT, SCRIPT_EC2_PURCHASE_OPTION_PARTIAL_UPFRONT)



EC2_PURCHASE_OPTION_MAP = {SCRIPT_EC2_PURCHASE_OPTION_PARTIAL_UPFRONT:EC2_PURCHASE_OPTION_PARTIAL_UPFRONT,
                           SCRIPT_EC2_PURCHASE_OPTION_ALL_UPFRONT: EC2_PURCHASE_OPTION_ALL_UPFRONT, SCRIPT_EC2_PURCHASE_OPTION_NO_UPFRONT: EC2_PURCHASE_OPTION_NO_UPFRONT
                           }

SUPPORTED_EC2_OPERATING_SYSTEMS = (SCRIPT_OPERATING_SYSTEM_LINUX,
                                   SCRIPT_OPERATING_SYSTEM_WINDOWS,
                                   SCRIPT_OPERATING_SYSTEM_WINDOWS_BYOL,
                                   SCRIPT_OPERATING_SYSTEM_SUSE,
                                   #SCRIPT_OPERATING_SYSTEM_SQL_WEB,
                                   SCRIPT_OPERATING_SYSTEM_RHEL)

SUPPORTED_EC2_LICENSE_MODELS = (SCRIPT_EC2_LICENSE_MODEL_BYOL, SCRIPT_EC2_LICENSE_MODEL_INCLUDED, SCRIPT_EC2_LICENSE_MODEL_NONE_REQUIRED)

EC2_LICENSE_MODEL_MAP = {SCRIPT_EC2_LICENSE_MODEL_BYOL: 'Bring your own license',
                         SCRIPT_EC2_LICENSE_MODEL_INCLUDED: 'License Included',
                         SCRIPT_EC2_LICENSE_MODEL_NONE_REQUIRED: 'No License required'
                         }


EC2_OPERATING_SYSTEMS_MAP = {SCRIPT_OPERATING_SYSTEM_LINUX:'Linux',
                             SCRIPT_OPERATING_SYSTEM_WINDOWS_BYOL:'Windows',
                             SCRIPT_OPERATING_SYSTEM_WINDOWS:'Windows',
                             SCRIPT_OPERATING_SYSTEM_SUSE:'SUSE',
                             #SCRIPT_OPERATING_SYSTEM_SQL_WEB:'SQL Web',
                             SCRIPT_OPERATING_SYSTEM_RHEL:'RHEL'}

SUPPORTED_EBS_VOLUME_TYPES = (SCRIPT_EBS_VOLUME_TYPE_STANDARD,
                             SCRIPT_EBS_VOLUME_TYPE_IO1,
                             SCRIPT_EBS_VOLUME_TYPE_GP2,
                             SCRIPT_EBS_VOLUME_TYPE_SC1,
                             SCRIPT_EBS_VOLUME_TYPE_ST1
                             )

EBS_VOLUME_TYPES_MAP = {
                        SCRIPT_EBS_VOLUME_TYPE_STANDARD : {'storageMedia':STORAGE_MEDIA_HDD , 'volumeType':EBS_VOLUME_TYPE_MAGNETIC},
                        SCRIPT_EBS_VOLUME_TYPE_IO1 : {'storageMedia':STORAGE_MEDIA_SSD , 'volumeType':EBS_VOLUME_TYPE_PIOPS},
                        SCRIPT_EBS_VOLUME_TYPE_GP2 : {'storageMedia':STORAGE_MEDIA_SSD , 'volumeType':EBS_VOLUME_TYPE_GENERAL_PURPOSE},
                        SCRIPT_EBS_VOLUME_TYPE_SC1 : {'storageMedia':STORAGE_MEDIA_HDD , 'volumeType':EBS_VOLUME_TYPE_COLD_HDD},
                        SCRIPT_EBS_VOLUME_TYPE_ST1 : {'storageMedia':STORAGE_MEDIA_HDD , 'volumeType':EBS_VOLUME_TYPE_THROUGHPUT_OPTIMIZED}
                       }

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

#RDS

SUPPORTED_RDS_INSTANCE_CLASSES = ('db.t1.micro', 'db.m1.small', 'db.m1.medium', 'db.m1.large', 'db.m1.xlarge',
                'db.m2.xlarge', 'db.m2.2xlarge', 'db.m2.4xlarge',
                'db.m3.medium', 'db.m3.large', 'db.m3.xlarge', 'db.m3.2xlarge',
                'db.m4.large', 'db.m4.xlarge', 'db.m4.2xlarge', 'db.m4.4xlarge', 'db.m4.10xlarge', 'db.m4.16xlarge',
                'db.r3.large', 'db.r3.xlarge', 'db.r3.2xlarge', 'db.r3.4xlarge', 'db.r3.8xlarge',
                'db.r4.large', 'db.r4.xlarge', 'db.r4.2xlarge', 'db.r4.4xlarge', 'db.r4.8xlarge', 'db.r4.16xlarge',
                'db.t2.micro', 'db.t2.small', 'db.t2.2xlarge', 'db.t2.large', 'db.t2.xlarge', 'db.t2.medium')


SCRIPT_RDS_STORAGE_TYPE_STANDARD = 'standard'
SCRIPT_RDS_STORAGE_TYPE_AURORA = 'aurora' #Aurora has its own type of storage, which is billed by IO operations and size
SCRIPT_RDS_STORAGE_TYPE_GP2 = 'gp2'
SCRIPT_RDS_STORAGE_TYPE_IO1 = 'io1'

RDS_VOLUME_TYPE_MAGNETIC = 'Magnetic'
RDS_VOLUME_TYPE_AURORA = 'General Purpose-Aurora'
RDS_VOLUME_TYPE_GP2 = 'General Purpose'
RDS_VOLUME_TYPE_IO1 = 'Provisioned IOPS'




RDS_VOLUME_TYPES_MAP = {
                        SCRIPT_RDS_STORAGE_TYPE_STANDARD : RDS_VOLUME_TYPE_MAGNETIC,
                        SCRIPT_RDS_STORAGE_TYPE_AURORA : RDS_VOLUME_TYPE_AURORA,
                        SCRIPT_RDS_STORAGE_TYPE_GP2 : RDS_VOLUME_TYPE_GP2,
                        SCRIPT_RDS_STORAGE_TYPE_IO1 : RDS_VOLUME_TYPE_IO1
                       }



SUPPORTED_RDS_STORAGE_TYPES = (SCRIPT_RDS_STORAGE_TYPE_STANDARD, SCRIPT_RDS_STORAGE_TYPE_AURORA, SCRIPT_RDS_STORAGE_TYPE_GP2, SCRIPT_RDS_STORAGE_TYPE_IO1)


RDS_DEPLOYMENT_OPTION_SINGLE_AZ = 'Single-AZ'
RDS_DEPLOYMENT_OPTION_MULTI_AZ = 'Multi-AZ'
RDS_DEPLOYMENT_OPTION_MULTI_AZ_MIRROR = 'Multi-AZ (SQL Server Mirror)'

RDS_DB_ENGINE_MYSQL = 'MySQL'
RDS_DB_ENGINE_MARIADB = 'MariaDB'
RDS_DB_ENGINE_ORACLE = 'Oracle'
RDS_DB_ENGINE_SQL_SERVER = 'SQL Server'
RDS_DB_ENGINE_POSTGRESQL = 'PostgreSQL'
RDS_DB_ENGINE_AURORA_MYSQL = 'Aurora MySQL'
RDS_DB_ENGINE_AURORA_POSTGRESQL = 'Aurora PostgreSQL'

RDS_DB_EDITION_ENTERPRISE = 'Enterprise'
RDS_DB_EDITION_STANDARD = 'Standard'
RDS_DB_EDITION_STANDARD_ONE = 'Standard One'
RDS_DB_EDITION_STANDARD_TWO = 'Standard Two'
RDS_DB_EDITION_EXPRESS = 'Express'
RDS_DB_EDITION_WEB = 'Web'


SCRIPT_RDS_DATABASE_ENGINE_MYSQL = 'mysql'
SCRIPT_RDS_DATABASE_ENGINE_MARIADB = 'mariadb'
SCRIPT_RDS_DATABASE_ENGINE_ORACLE_STANDARD = 'oracle-se'
SCRIPT_RDS_DATABASE_ENGINE_ORACLE_STANDARD_ONE = 'oracle-se1'
SCRIPT_RDS_DATABASE_ENGINE_ORACLE_STANDARD_TWO = 'oracle-se2'
SCRIPT_RDS_DATABASE_ENGINE_ORACLE_ENTERPRISE = 'oracle-ee'
SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_ENTERPRISE = 'sqlserver-ee'
SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_STANDARD = 'sqlserver-se'
SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_EXPRESS = 'sqlserver-ex'
SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_WEB = 'sqlserver-web'
SCRIPT_RDS_DATABASE_ENGINE_POSTGRESQL = 'postgres'
SCRIPT_RDS_DATABASE_ENGINE_AURORA_MYSQL = 'aurora'
SCRIPT_RDS_DATABASE_ENGINE_AURORA_POSTGRESQL = 'aurora-postgresql'

RDS_SUPPORTED_DB_ENGINES = (SCRIPT_RDS_DATABASE_ENGINE_MYSQL,SCRIPT_RDS_DATABASE_ENGINE_MARIADB,
                            SCRIPT_RDS_DATABASE_ENGINE_ORACLE_STANDARD, SCRIPT_RDS_DATABASE_ENGINE_ORACLE_STANDARD_ONE,
                            SCRIPT_RDS_DATABASE_ENGINE_ORACLE_STANDARD_TWO,SCRIPT_RDS_DATABASE_ENGINE_ORACLE_ENTERPRISE,
                            SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_ENTERPRISE, SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_STANDARD,
                            SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_EXPRESS, SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_WEB,
                            SCRIPT_RDS_DATABASE_ENGINE_POSTGRESQL, SCRIPT_RDS_DATABASE_ENGINE_AURORA_MYSQL,
                            SCRIPT_RDS_DATABASE_ENGINE_AURORA_POSTGRESQL
                            )

SCRIPT_RDS_LICENSE_MODEL_INCLUDED = 'license-included'
SCRIPT_RDS_LICENSE_MODEL_BYOL = 'bring-your-own-license'
SCRIPT_RDS_LICENSE_MODEL_PUBLIC = 'general-public-license'
RDS_SUPPORTED_LICENSE_MODELS = (SCRIPT_RDS_LICENSE_MODEL_INCLUDED, SCRIPT_RDS_LICENSE_MODEL_BYOL, SCRIPT_RDS_LICENSE_MODEL_PUBLIC)
RDS_LICENSE_MODEL_MAP = {SCRIPT_RDS_LICENSE_MODEL_INCLUDED:'License included',
                         SCRIPT_RDS_LICENSE_MODEL_BYOL:'Bring your own license',
                         SCRIPT_RDS_LICENSE_MODEL_PUBLIC:'No license required'}

RDS_ENGINE_MAP = {SCRIPT_RDS_DATABASE_ENGINE_MYSQL:{'engine':RDS_DB_ENGINE_MYSQL,'edition':''},
                  SCRIPT_RDS_DATABASE_ENGINE_MARIADB:{'engine':RDS_DB_ENGINE_MARIADB ,'edition':''},
                  SCRIPT_RDS_DATABASE_ENGINE_ORACLE_STANDARD:{'engine':RDS_DB_ENGINE_ORACLE ,'edition':RDS_DB_EDITION_STANDARD},
                  SCRIPT_RDS_DATABASE_ENGINE_ORACLE_STANDARD_ONE:{'engine':RDS_DB_ENGINE_ORACLE ,'edition':RDS_DB_EDITION_STANDARD_ONE},
                  SCRIPT_RDS_DATABASE_ENGINE_ORACLE_STANDARD_TWO:{'engine':RDS_DB_ENGINE_ORACLE ,'edition':RDS_DB_EDITION_STANDARD_TWO},
                  SCRIPT_RDS_DATABASE_ENGINE_ORACLE_ENTERPRISE:{'engine':RDS_DB_ENGINE_ORACLE ,'edition':RDS_DB_EDITION_ENTERPRISE},
                  SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_ENTERPRISE:{'engine':RDS_DB_ENGINE_SQL_SERVER ,'edition':RDS_DB_EDITION_ENTERPRISE},
                  SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_STANDARD:{'engine':RDS_DB_ENGINE_SQL_SERVER ,'edition':RDS_DB_EDITION_STANDARD},
                  SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_EXPRESS:{'engine':RDS_DB_ENGINE_SQL_SERVER ,'edition':RDS_DB_EDITION_EXPRESS},
                  SCRIPT_RDS_DATABASE_ENGINE_SQL_SERVER_WEB:{'engine':RDS_DB_ENGINE_SQL_SERVER ,'edition':RDS_DB_EDITION_WEB},
                  SCRIPT_RDS_DATABASE_ENGINE_POSTGRESQL:{'engine':RDS_DB_ENGINE_POSTGRESQL ,'edition':''},
                  SCRIPT_RDS_DATABASE_ENGINE_AURORA_MYSQL:{'engine':RDS_DB_ENGINE_AURORA_MYSQL ,'edition':''},
                  SCRIPT_RDS_DATABASE_ENGINE_AURORA_POSTGRESQL:{'engine':RDS_DB_ENGINE_AURORA_POSTGRESQL ,'edition':''}
                  }



#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

#S3

S3_USAGE_GROUP_REQUESTS_TIER_1 = 'S3-API-Tier1'
S3_USAGE_GROUP_REQUESTS_TIER_2 = 'S3-API-Tier2'
S3_USAGE_GROUP_REQUESTS_TIER_3 = 'S3-API-Tier3'
S3_USAGE_GROUP_REQUESTS_SIA_TIER1 = 'S3-API-SIA-Tier1'
S3_USAGE_GROUP_REQUESTS_SIA_TIER2 = 'S3-API-SIA-Tier2'
S3_USAGE_GROUP_REQUESTS_SIA_RETRIEVAL = 'S3-API-SIA-Retrieval'
S3_USAGE_GROUP_REQUESTS_ZIA_TIER1 = 'S3-API-ZIA-Tier1'
S3_USAGE_GROUP_REQUESTS_ZIA_TIER2 = 'S3-API-ZIA-Tier2'
S3_USAGE_GROUP_REQUESTS_ZIA_RETRIEVAL = 'S3-API-ZIA-Retrieval'


S3_STORAGE_CLASS_STANDARD = 'General Purpose'
S3_STORAGE_CLASS_SIA  = 'Infrequent Access'
S3_STORAGE_CLASS_ZIA = 'Infrequent Access'
S3_STORAGE_CLASS_GLACIER = 'Archive'
S3_STORAGE_CLASS_REDUCED_REDUNDANCY = 'Non-Critical Data'


SUPPORTED_REQUEST_TYPES = ('PUT','COPY','POST','LIST','GET')

SCRIPT_STORAGE_CLASS_INFREQUENT_ACCESS = 'STANDARD_IA'
SCRIPT_STORAGE_CLASS_ONE_ZONE_INFREQUENT_ACCESS = 'ONEZONE_IA'
SCRIPT_STORAGE_CLASS_STANDARD = 'STANDARD'
SCRIPT_STORAGE_CLASS_GLACIER = 'GLACIER'
SCRIPT_STORAGE_CLASS_REDUCED_REDUNDANCY = 'REDUCED_REDUNDANCY'

SUPPORTED_S3_STORAGE_CLASSES = (SCRIPT_STORAGE_CLASS_STANDARD,
                             SCRIPT_STORAGE_CLASS_INFREQUENT_ACCESS,
                             SCRIPT_STORAGE_CLASS_ONE_ZONE_INFREQUENT_ACCESS,
                             SCRIPT_STORAGE_CLASS_GLACIER,
                             SCRIPT_STORAGE_CLASS_REDUCED_REDUNDANCY)

S3_STORAGE_CLASS_MAP = {SCRIPT_STORAGE_CLASS_INFREQUENT_ACCESS:S3_STORAGE_CLASS_SIA,
                        SCRIPT_STORAGE_CLASS_ONE_ZONE_INFREQUENT_ACCESS:S3_STORAGE_CLASS_ZIA,
                        SCRIPT_STORAGE_CLASS_STANDARD:S3_STORAGE_CLASS_STANDARD,
                        SCRIPT_STORAGE_CLASS_GLACIER:S3_STORAGE_CLASS_GLACIER,
                        SCRIPT_STORAGE_CLASS_REDUCED_REDUNDANCY:S3_STORAGE_CLASS_REDUCED_REDUNDANCY}

S3_USAGE_TYPE_DICT = {
                       SCRIPT_STORAGE_CLASS_STANDARD:'TimedStorage-ByteHrs',
                       SCRIPT_STORAGE_CLASS_INFREQUENT_ACCESS:'TimedStorage-SIA-ByteHrs',
                       SCRIPT_STORAGE_CLASS_ONE_ZONE_INFREQUENT_ACCESS:'TimedStorage-ZIA-ByteHrs',
                       SCRIPT_STORAGE_CLASS_GLACIER:'TimedStorage-GlacierByteHrs',
                       SCRIPT_STORAGE_CLASS_REDUCED_REDUNDANCY:'TimedStorage-RRS-ByteHrs'
                       }

S3_VOLUME_TYPE_DICT = {
                       SCRIPT_STORAGE_CLASS_STANDARD:'Standard',
                       SCRIPT_STORAGE_CLASS_INFREQUENT_ACCESS:'Standard - Infrequent Access',
                       SCRIPT_STORAGE_CLASS_ONE_ZONE_INFREQUENT_ACCESS:'One Zone - Infrequent Access',
                       SCRIPT_STORAGE_CLASS_GLACIER:'Amazon Glacier',
                       SCRIPT_STORAGE_CLASS_REDUCED_REDUNDANCY:'Reduced Redundancy'
                       }




#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

#LAMBDA

LAMBDA_MEM_SIZES = [64,128,192,256,320,384,448,512,576,640,704,768,832,896,960,1024,1088,1152,1216,1280,1344,1408,
                    1472,1536,1600,1664,1728,1792,1856,1920,1984,2048,2112,2176,2240,2304,2368,2432,2496,2560,2624,2688,
                    2752,2816,2880,2944,3008]
