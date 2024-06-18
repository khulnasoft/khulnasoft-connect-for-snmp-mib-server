#
# PySNMP MIB module DKSF-707-1-X-X-1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DKSF-707-1-X-X-1
# Produced by pysmi-0.3.4 at Mon Apr 29 18:32:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
enterprises, TimeTicks, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, IpAddress, MibIdentifier, ModuleIdentity, Unsigned32, Counter64, Integer32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "TimeTicks", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "IpAddress", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Counter64", "Integer32", "Counter32", "iso")
TimeStamp, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString", "TruthValue")
uniPingServerSolutionV3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25728, 707))
uniPingServerSolutionV3.setRevisions(('2014-03-03 00:00',))
if mibBuilder.loadTexts: uniPingServerSolutionV3.setLastUpdated('201403030000Z')
if mibBuilder.loadTexts: uniPingServerSolutionV3.setOrganization('Alentis Electronics')
lightcom = MibIdentifier((1, 3, 6, 1, 4, 1, 25728))
npTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 90))
npTrapEmailTo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 90, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npTrapEmailTo.setStatus('current')
npGsm = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800))
npGsmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 1))
npGsmFailed = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ok", 0), ("failed", 1), ("fatalError", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmFailed.setStatus('current')
npGsmRegistration = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 255))).clone(namedValues=NamedValues(("impossible", 0), ("homeNetwork", 1), ("searching", 2), ("denied", 3), ("unknown", 4), ("roaming", 5), ("infoUpdate", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmRegistration.setStatus('current')
npGsmStrength = MibScalar((1, 3, 6, 1, 4, 1, 25728, 3800, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npGsmStrength.setStatus('current')
npGsmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 2))
npGsmTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0))
npGsmTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0, 1)).setObjects(("DKSF-707-1-X-X-1", "npGsmFailed"), ("DKSF-707-1-X-X-1", "npGsmRegistration"), ("DKSF-707-1-X-X-1", "npGsmStrength"))
if mibBuilder.loadTexts: npGsmTrap.setStatus('current')
npReboot = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 911))
npSoftReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npSoftReboot.setStatus('current')
npResetStack = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npResetStack.setStatus('current')
npForcedReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npForcedReboot.setStatus('current')
mibBuilder.exportSymbols("DKSF-707-1-X-X-1", npTrapEmailTo=npTrapEmailTo, npGsm=npGsm, npResetStack=npResetStack, npForcedReboot=npForcedReboot, PYSNMP_MODULE_ID=uniPingServerSolutionV3, npGsmTrap=npGsmTrap, lightcom=lightcom, npReboot=npReboot, npSoftReboot=npSoftReboot, npTrapInfo=npTrapInfo, uniPingServerSolutionV3=uniPingServerSolutionV3, npGsmStrength=npGsmStrength, npGsmTrapPrefix=npGsmTrapPrefix, npGsmTraps=npGsmTraps, npGsmInfo=npGsmInfo, npGsmFailed=npGsmFailed, npGsmRegistration=npGsmRegistration)
