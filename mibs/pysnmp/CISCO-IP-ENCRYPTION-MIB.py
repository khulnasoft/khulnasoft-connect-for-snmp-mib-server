#
# PySNMP MIB module CISCO-IP-ENCRYPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-ENCRYPTION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
OwnerString, = mibBuilder.importSymbols("IF-MIB", "OwnerString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, Counter32, Bits, ModuleIdentity, ObjectIdentity, Integer32, TimeTicks, IpAddress, Gauge32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Counter32", "Bits", "ModuleIdentity", "ObjectIdentity", "Integer32", "TimeTicks", "IpAddress", "Gauge32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
DisplayString, RowStatus, TruthValue, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString", "RowStatus", "TruthValue", "TimeStamp")
ciscoIpEncryptionMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52))
ciscoIpEncryptionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 1))
cieConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 1))
cieEngineStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2))
cieConnections = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3))
cieTestConnection = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4))
cieMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 2))
cieMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 2, 0))
cieMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 3))
cieMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 3, 1))
cieMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 3, 2))
cieConfiguredAlgorithms = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieConfiguredAlgorithms.setStatus('mandatory')
cieEncryptionKeyTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieEncryptionKeyTimeout.setStatus('mandatory')
cieNumberOfCryptoEngines = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieNumberOfCryptoEngines.setStatus('mandatory')
cieEngineStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1), )
if mibBuilder.loadTexts: cieEngineStatusTable.setStatus('mandatory')
cieEngineStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-IP-ENCRYPTION-MIB", "cieEngineID"))
if mibBuilder.loadTexts: cieEngineStatusEntry.setStatus('mandatory')
cieEngineID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieEngineID.setStatus('mandatory')
cieEngineCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieEngineCardIndex.setStatus('mandatory')
cieEnginePublicKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieEnginePublicKey.setStatus('mandatory')
cieEsaTampered = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieEsaTampered.setStatus('mandatory')
cieEsaAuthenticated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieEsaAuthenticated.setStatus('mandatory')
cieEsaMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enableActive", 1), ("boot", 2), ("error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieEsaMode.setStatus('mandatory')
cieNumberOfConnections = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieNumberOfConnections.setStatus('mandatory')
cieConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2), )
if mibBuilder.loadTexts: cieConnTable.setStatus('mandatory')
cieConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-IP-ENCRYPTION-MIB", "cieEngineID"), (0, "CISCO-IP-ENCRYPTION-MIB", "cieConnIndex"))
if mibBuilder.loadTexts: cieConnEntry.setStatus('mandatory')
cieConnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cieConnIndex.setStatus('mandatory')
cieProtectedAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieProtectedAddr.setStatus('mandatory')
cieUnprotectedAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieUnprotectedAddr.setStatus('mandatory')
cieConnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pendingConnection", 1), ("openConnection", 2), ("exchangeKeys", 3), ("badConnection", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieConnStatus.setStatus('mandatory')
ciePktsEncrypted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciePktsEncrypted.setStatus('mandatory')
ciePktsDecrypted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciePktsDecrypted.setStatus('mandatory')
ciePktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciePktsDropped.setStatus('mandatory')
cieLocalTimeEstablished = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieLocalTimeEstablished.setStatus('mandatory')
cieAlgorithmType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("des56bitCfb64", 1), ("des56bitCfb8", 2), ("des40bitCfb64", 3), ("des40bitdesCfb8", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieAlgorithmType.setStatus('mandatory')
cieTestConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1), )
if mibBuilder.loadTexts: cieTestConnTable.setStatus('mandatory')
cieTestConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-IP-ENCRYPTION-MIB", "cieTestConnSerialNumber"))
if mibBuilder.loadTexts: cieTestConnEntry.setStatus('mandatory')
cieTestConnSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cieTestConnSerialNumber.setStatus('mandatory')
cieTestConnProtectedAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieTestConnProtectedAddr.setStatus('mandatory')
cieTestConnUnprotectedAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieTestConnUnprotectedAddr.setStatus('mandatory')
cieTestConnTrapOnCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieTestConnTrapOnCompletion.setStatus('mandatory')
cieTestConnCryptoMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieTestConnCryptoMapName.setStatus('mandatory')
cieTestConnCryptoMapTagNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieTestConnCryptoMapTagNumber.setStatus('mandatory')
cieTestConnSessionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inProgress", 1), ("fail", 2), ("success", 3), ("badCryptoMapName", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cieTestConnSessionStatus.setStatus('mandatory')
cieTestConnEntryOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 8), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieTestConnEntryOwner.setStatus('mandatory')
cieTestConnEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 52, 1, 4, 1, 1, 9), RowStatus().clone('createAndGo')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cieTestConnEntryStatus.setStatus('mandatory')
cieTestCompletion = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 52, 2) + (0,1)).setObjects(("CISCO-IP-ENCRYPTION-MIB", "cieTestConnSessionStatus"), ("CISCO-IP-ENCRYPTION-MIB", "cieTestConnProtectedAddr"), ("CISCO-IP-ENCRYPTION-MIB", "cieTestConnUnprotectedAddr"))
cieMIBGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 3, 2, 1))
cieMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 52, 3, 1, 1))
mibBuilder.exportSymbols("CISCO-IP-ENCRYPTION-MIB", cieMIBTraps=cieMIBTraps, cieMIBTrapPrefix=cieMIBTrapPrefix, cieMIBCompliance=cieMIBCompliance, cieTestConnTable=cieTestConnTable, cieMIBGroups=cieMIBGroups, cieEsaMode=cieEsaMode, ciePktsDropped=ciePktsDropped, cieTestConnCryptoMapTagNumber=cieTestConnCryptoMapTagNumber, cieConnTable=cieConnTable, cieEsaTampered=cieEsaTampered, cieNumberOfCryptoEngines=cieNumberOfCryptoEngines, ciscoIpEncryptionMIB=ciscoIpEncryptionMIB, cieTestConnEntryOwner=cieTestConnEntryOwner, cieMIBCompliances=cieMIBCompliances, cieEngineStatusTable=cieEngineStatusTable, cieConnStatus=cieConnStatus, cieConnEntry=cieConnEntry, cieMIBConformance=cieMIBConformance, cieEnginePublicKey=cieEnginePublicKey, cieTestCompletion=cieTestCompletion, cieTestConnSessionStatus=cieTestConnSessionStatus, cieEngineStatus=cieEngineStatus, ciePktsDecrypted=ciePktsDecrypted, cieEngineID=cieEngineID, ciscoIpEncryptionMIBObjects=ciscoIpEncryptionMIBObjects, cieConfig=cieConfig, cieTestConnUnprotectedAddr=cieTestConnUnprotectedAddr, cieMIBGroup=cieMIBGroup, cieTestConnTrapOnCompletion=cieTestConnTrapOnCompletion, cieTestConnEntryStatus=cieTestConnEntryStatus, cieEsaAuthenticated=cieEsaAuthenticated, ciePktsEncrypted=ciePktsEncrypted, cieNumberOfConnections=cieNumberOfConnections, cieTestConnCryptoMapName=cieTestConnCryptoMapName, cieTestConnection=cieTestConnection, cieLocalTimeEstablished=cieLocalTimeEstablished, cieAlgorithmType=cieAlgorithmType, cieEngineCardIndex=cieEngineCardIndex, cieConnIndex=cieConnIndex, cieTestConnEntry=cieTestConnEntry, cieTestConnProtectedAddr=cieTestConnProtectedAddr, cieEncryptionKeyTimeout=cieEncryptionKeyTimeout, cieTestConnSerialNumber=cieTestConnSerialNumber, cieConfiguredAlgorithms=cieConfiguredAlgorithms, cieConnections=cieConnections, cieUnprotectedAddr=cieUnprotectedAddr, cieProtectedAddr=cieProtectedAddr, cieEngineStatusEntry=cieEngineStatusEntry)
