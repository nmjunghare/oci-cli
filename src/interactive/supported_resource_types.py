supported_resource_types = set(
    [
        "AiAnomalyDetectionDataAsset",
        "AiAnomalyDetectionModel",
        "AiAnomalyDetectionProject",
        "AiAnomalyDetectionPvtEndpoint",
        "AiVisionModel",
        "AiVisionProject",
        "Alarm",
        "AmsMigration",
        "AmsSource",
        "AnalyticsInstance",
        "ApiDeployment",
        "ApiGateway",
        "ApiGatewayApi",
        "ApiGatewayCertificate",
        "ApiGatewaySdk",
        "ApmDomain",
        "App",
        "AutoScalingConfiguration",
        "AutonomousContainerDatabase",
        "AutonomousDataSecurityInstance",
        "AutonomousDatabase",
        "AutonomousExadataInfrastructure",
        "AutonomousVmCluster",
        "BackupDestination",
        "Bastion",
        "BigDataService",
        "BigDataServiceApiKey",
        "BigDataServiceMetastoreConfig",
        "BlockchainPlatform",
        "BootVolume",
        "BootVolumeBackup",
        "BootVolumeReplica",
        "Bucket",
        "Budget",
        "ByoipRange",
        "CaBundle",
        "CaBundleAssociation",
        "Certificate",
        "CertificateAssociation",
        "CertificateAuthority",
        "CertificateAuthorityAssociation",
        "CloudExadataInfrastructure",
        "CloudGuardDetectorRecipe",
        "CloudGuardManagedList",
        "CloudGuardResponderRecipe",
        "CloudGuardTarget",
        "CloudVmCluster",
        "ClusterNetwork",
        "Compartment",
        "ComputeCapacityReservation",
        "ConnectHarness",
        "ConsoleDashboard",
        "ConsoleDashboardGroup",
        "ConsoleHistory",
        "ContainerImage",
        "ContainerRepo",
        "ContinuousQuery",
        "Cpe",
        "CrossConnect",
        "CrossConnectGroup",
        "CustomerDnsZone",
        "DCMSEndpoint",
        "DCMSRegistry",
        "DHCPOptions",
        "DISWorkspace",
        "DataCatalog",
        "DataCatalogMetastore",
        "DataCatalogPrivateEndpoint",
        "DataFlowApplication",
        "DataFlowCluster",
        "DataFlowRun",
        "DataLabelingDataset",
        "DataSafeAlertPolicy",
        "DataSafeArchiveRetrieval",
        "DataSafeAuditPolicy",
        "DataSafeAuditProfile",
        "DataSafeAuditTrail",
        "DataSafeDiscoveryJob",
        "DataSafeLibraryMaskingFormat",
        "DataSafeMaskingPolicy",
        "DataSafeMaskingReport",
        "DataSafeOnpremConnector",
        "DataSafePrivateEndpoint",
        "DataSafeReport",
        "DataSafeReportDefinition",
        "DataSafeSecurityAssessment",
        "DataSafeSensitiveDataModel",
        "DataSafeSensitiveType",
        "DataSafeTargetDatabase",
        "DataSafeUserAssessment",
        "DataScienceJob",
        "DataScienceJobRun",
        "DataScienceModel",
        "DataScienceModelDeployment",
        "DataScienceNotebookSession",
        "DataScienceProject",
        "DataTransferAppliance",
        "DataTransferApplianceExportJob",
        "DataTransferDevice",
        "DataTransferJob",
        "DataTransferPackage",
        "Database",
        "DatabaseSoftwareImage",
        "DatabaseToolsConnection",
        "DatabaseToolsPrivateEndpoint",
        "DbHome",
        "DbKeyStore",
        "DbServer",
        "DbSystem",
        "DedicatedVmHost",
        "DevOpsBuildPipeline",
        "DevOpsBuildPipelineStage",
        "DevOpsBuildRun",
        "DevOpsConnection",
        "DevOpsDeployArtifact",
        "DevOpsDeployEnvironment",
        "DevOpsDeployPipeline",
        "DevOpsDeployStage",
        "DevOpsDeployment",
        "DevOpsProject",
        "DevOpsRepository",
        "DevOpsTrigger",
        "DnsPolicy",
        "DnsPolicyAttachment",
        "DnsResolver",
        "DnsTsigKey",
        "DnsView",
        "Drg",
        "DrgAttachment",
        "DrgRouteDistribution",
        "DrgRouteTable",
        "DynamicResourceGroup",
        "EmailDkim",
        "EmailDomain",
        "EmailSender",
        "EventRule",
        "ExadataInfrastructure",
        "Export",
        "ExternalContainerDatabase",
        "ExternalDatabaseConnector",
        "ExternalNonContainerDatabase",
        "ExternalPluggableDatabase",
        "FileSystem",
        "FssReplication",
        "FssReplicationTarget",
        "FunctionsApplication",
        "FunctionsFunction",
        "GoldenGateDatabaseRegistration",
        "GoldenGateDeployment",
        "GoldenGateDeploymentBackup",
        "Group",
        "HttpRedirect",
        "IPSecConnection",
        "IdentityProvider",
        "Image",
        "Instance",
        "InstanceConfiguration",
        "InstancePool",
        "IntegrationInstance",
        "InternetGateway",
        "Ipv6",
        "Key",
        "LoadBalancer",
        "LocalPeeringGateway",
        "Log",
        "LogAnalyticsEntity",
        "LogDataModel",
        "LogGroup",
        "LogSavedSearch",
        "ManagementAgent",
        "ManagementAgentInstallKey",
        "MountTarget",
        "NatGateway",
        "NetworkSecurityGroup",
        "NoSQLTable",
        "OceInstance",
        "OdaInstance",
        "OdmsAgent",
        "OdmsConnection",
        "OdmsJob",
        "OdmsMigration",
        "OnsSubscription",
        "OnsTopic",
        "OpctlOperatorControl",
        "OpctlOperatorControlAssignment",
        "OrmConfigSourceProvider",
        "OrmJob",
        "OrmStack",
        "OrmTemplate",
        "OsmsManagedInstanceGroup",
        "OsmsScheduledJob",
        "OsmsSoftwareSource",
        "OutboundConnector",
        "PathAnalyzerTest",
        "PluggableDatabase",
        "Policy",
        "PrivateIp",
        "PublicIp",
        "PublicIpPool",
        "Quota",
        "RemotePeeringConnection",
        "RouteTable",
        "SecurityList",
        "ServiceConnector",
        "ServiceGateway",
        "StorageGateway",
        "Stream",
        "Subnet",
        "TagDefault",
        "TagNamespace",
        "UnifiedAgentConfiguration",
        "User",
        "Vault",
        "VaultSecret",
        "Vcn",
        "VirtualCircuit",
        "VisualBuilderInstance",
        "Vlan",
        "VmCluster",
        "VmClusterNetwork",
        "VmwareEsxiHost",
        "VmwareSddc",
        "Vnic",
        "Volume",
        "VolumeBackup",
        "VolumeBackupPolicy",
        "VolumeGroup",
        "VolumeGroupBackup",
        "VolumeGroupReplica",
        "VolumeReplica",
        "VssContainerScanRecipe",
        "VssContainerScanTarget",
        "VssHostScanRecipe",
        "VssHostScanTarget",
        "WaasAddressList",
        "WaasCertificate",
        "WaasCustomProtectionRule",
        "WaasPolicy",
        "WebAppFirewall",
        "WebAppFirewallNetworkAddressList",
        "WebAppFirewallPolicy"
    ]
)