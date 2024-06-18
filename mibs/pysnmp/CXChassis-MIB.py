#
# PySNMP MIB module CXChassis-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXChassis-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:16:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cxChassis, cxRegChasCX1000 = mibBuilder.importSymbols("CXProduct-SMI", "cxChassis", "cxRegChasCX1000")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, ModuleIdentity, Unsigned32, Integer32, TimeTicks, Counter32, Counter64, ObjectIdentity, NotificationType, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "ModuleIdentity", "Unsigned32", "Integer32", "TimeTicks", "Counter32", "Counter64", "ObjectIdentity", "NotificationType", "NotificationType", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cxChasTrapCard = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxChasTrapCard.setStatus('mandatory')
cxFileTargetSlot = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFileTargetSlot.setStatus('mandatory')
cxChasSubSysTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5), )
if mibBuilder.loadTexts: cxChasSubSysTable.setStatus('mandatory')
cxChasSubSysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1), ).setIndexNames((0, "CXChassis-MIB", "cxChasSubSysSlotNb"))
if mibBuilder.loadTexts: cxChasSubSysEntry.setStatus('mandatory')
cxChasSubSysSlotNb = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysSlotNb.setStatus('mandatory')
cxChasSubSysDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysDesc.setStatus('mandatory')
cxChasSubSysObjectID = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysObjectID.setStatus('mandatory')
cxChasSubSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysName.setStatus('mandatory')
cxChasSubSysServices = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysServices.setStatus('mandatory')
cxChasSubSysVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysVersion.setStatus('mandatory')
cxChasSubSysOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noresponse", 1), ("responding", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysOperState.setStatus('mandatory')
cxChasSubSysConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("writetoflash", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cxChasSubSysConfig.setStatus('mandatory')
cxChasSubSysRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("warmstart-with-save", 1), ("coldstart", 2), ("warmstart-without-save", 3)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cxChasSubSysRestart.setStatus('mandatory')
cxChasCardUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 1) + (0,10)).setObjects(("CXChassis-MIB", "cxChasSubSysSlotNb"))
cxChasCardDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 1) + (0,11)).setObjects(("CXChassis-MIB", "cxChasSubSysSlotNb"))
chassisMibLevel = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMibLevel.setStatus('mandatory')
mibBuilder.exportSymbols("CXChassis-MIB", cxChasSubSysDesc=cxChasSubSysDesc, cxChasSubSysOperState=cxChasSubSysOperState, cxChasTrapCard=cxChasTrapCard, cxChasCardUpTrap=cxChasCardUpTrap, cxChasSubSysName=cxChasSubSysName, chassisMibLevel=chassisMibLevel, cxChasSubSysObjectID=cxChasSubSysObjectID, cxFileTargetSlot=cxFileTargetSlot, cxChasSubSysVersion=cxChasSubSysVersion, cxChasSubSysConfig=cxChasSubSysConfig, cxChasSubSysSlotNb=cxChasSubSysSlotNb, cxChasSubSysEntry=cxChasSubSysEntry, cxChasSubSysServices=cxChasSubSysServices, cxChasSubSysTable=cxChasSubSysTable, cxChasSubSysRestart=cxChasSubSysRestart, cxChasCardDownTrap=cxChasCardDownTrap)
