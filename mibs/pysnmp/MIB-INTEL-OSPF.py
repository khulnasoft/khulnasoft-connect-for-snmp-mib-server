#
# PySNMP MIB module MIB-INTEL-OSPF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MIB-INTEL-OSPF
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mib2ext, = mibBuilder.importSymbols("INTEL-GEN-MIB", "mib2ext")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, Counter32, NotificationType, Unsigned32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, ModuleIdentity, Gauge32, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter32", "NotificationType", "Unsigned32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Gauge32", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ospf = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 6, 40))
ospfIpRouteTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 40, 1), )
if mibBuilder.loadTexts: ospfIpRouteTable.setStatus('optional')
ospfIpRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1), ).setIndexNames((0, "MIB-INTEL-OSPF", "ospfIpRouteChassis"), (0, "MIB-INTEL-OSPF", "ospfIpRouteModule"), (0, "MIB-INTEL-OSPF", "ospfIpRouteInst"), (0, "MIB-INTEL-OSPF", "ospfIpRouteDest"), (0, "MIB-INTEL-OSPF", "ospfIpRouteMask"), (0, "MIB-INTEL-OSPF", "ospfIpRouteIfIndex"), (0, "MIB-INTEL-OSPF", "ospfIpRouteNextHop"))
if mibBuilder.loadTexts: ospfIpRouteEntry.setStatus('optional')
ospfIpRouteChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfIpRouteChassis.setStatus('optional')
ospfIpRouteModule = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfIpRouteModule.setStatus('optional')
ospfIpRouteInst = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfIpRouteInst.setStatus('optional')
ospfIpRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfIpRouteDest.setStatus('optional')
ospfIpRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfIpRouteMask.setStatus('optional')
ospfIpRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfIpRouteIfIndex.setStatus('optional')
ospfIpRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfIpRouteNextHop.setStatus('optional')
ospfIpRoutePref = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfIpRoutePref.setStatus('optional')
ospfIpRouteCost = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfIpRouteCost.setStatus('optional')
ospfIpRouteState = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("dead", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfIpRouteState.setStatus('optional')
ospfIpRouteAge = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfIpRouteAge.setStatus('optional')
ospfIpRouteProtoType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("intraArea", 1), ("interArea", 2), ("ext1", 3), ("ext2", 4), ("type3Discard", 5), ("type7Discard", 6), ("other", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfIpRouteProtoType.setStatus('optional')
ospfIfCntTable = MibTable((1, 3, 6, 1, 4, 1, 343, 6, 40, 2), )
if mibBuilder.loadTexts: ospfIfCntTable.setStatus('optional')
ospfIfCntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1), ).setIndexNames((0, "MIB-INTEL-OSPF", "ospfCntChassis"), (0, "MIB-INTEL-OSPF", "ospfCntModule"), (0, "MIB-INTEL-OSPF", "ospfCntIfIpAddress"), (0, "MIB-INTEL-OSPF", "ospfCntAddressLessIf"))
if mibBuilder.loadTexts: ospfIfCntEntry.setStatus('optional')
ospfCntChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfCntChassis.setStatus('optional')
ospfCntModule = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfCntModule.setStatus('optional')
ospfCntIfIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfCntIfIpAddress.setStatus('optional')
ospfCntAddressLessIf = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ospfCntAddressLessIf.setStatus('optional')
ospfCntBadVer = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntBadVer.setStatus('optional')
ospfCntBadAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntBadAreaId.setStatus('optional')
ospfCntMaskMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 7), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntMaskMismatch.setStatus('optional')
ospfCntAuthMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 8), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntAuthMismatch.setStatus('optional')
ospfCntAuthFail = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntAuthFail.setStatus('optional')
ospfCntExtOptMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 10), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntExtOptMismatch.setStatus('optional')
ospfCntNSSAOptMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 11), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntNSSAOptMismatch.setStatus('optional')
ospfCntNBMANeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 12), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntNBMANeighbor.setStatus('optional')
ospfCntVirtNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 13), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntVirtNeighbor.setStatus('optional')
ospfCntHelloMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 14), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntHelloMismatch.setStatus('optional')
ospfCntDeadMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 15), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntDeadMismatch.setStatus('optional')
ospfCntBadType = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 16), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntBadType.setStatus('optional')
ospfCntBadChksum = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 17), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntBadChksum.setStatus('optional')
ospfCntBadLen = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 18), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntBadLen.setStatus('optional')
ospfCntTooShort = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 19), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntTooShort.setStatus('optional')
ospfCntDRPktMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 20), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntDRPktMismatch.setStatus('optional')
ospfCntMulticastVL = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 21), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntMulticastVL.setStatus('optional')
ospfCntDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 22), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntDestAddr.setStatus('optional')
ospfCntOwnAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 23), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntOwnAddr.setStatus('optional')
ospfCntHelloTx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 24), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntHelloTx.setStatus('optional')
ospfCntHelloRx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 25), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntHelloRx.setStatus('optional')
ospfCntLSReqTx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 26), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntLSReqTx.setStatus('optional')
ospfCntLSUpdateTx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 27), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntLSUpdateTx.setStatus('optional')
ospfCntLSAckTx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 28), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntLSAckTx.setStatus('optional')
ospfCntLSReqRx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 29), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntLSReqRx.setStatus('optional')
ospfCntLSUpdateRx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 30), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntLSUpdateRx.setStatus('optional')
ospfCntLSAckRx = MibTableColumn((1, 3, 6, 1, 4, 1, 343, 6, 40, 2, 1, 31), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfCntLSAckRx.setStatus('optional')
mibBuilder.exportSymbols("MIB-INTEL-OSPF", ospfIpRouteModule=ospfIpRouteModule, ospfCntModule=ospfCntModule, ospfCntIfIpAddress=ospfCntIfIpAddress, ospfCntAddressLessIf=ospfCntAddressLessIf, ospfCntDeadMismatch=ospfCntDeadMismatch, ospfCntHelloTx=ospfCntHelloTx, ospfIfCntTable=ospfIfCntTable, ospfCntLSReqRx=ospfCntLSReqRx, ospfIpRouteState=ospfIpRouteState, ospfCntAuthMismatch=ospfCntAuthMismatch, ospfCntBadChksum=ospfCntBadChksum, ospfIpRouteMask=ospfIpRouteMask, ospfCntDRPktMismatch=ospfCntDRPktMismatch, ospfCntLSAckRx=ospfCntLSAckRx, ospfIpRouteProtoType=ospfIpRouteProtoType, ospfCntHelloMismatch=ospfCntHelloMismatch, ospfCntVirtNeighbor=ospfCntVirtNeighbor, ospfCntHelloRx=ospfCntHelloRx, ospfCntLSReqTx=ospfCntLSReqTx, ospfIpRouteAge=ospfIpRouteAge, ospfCntMaskMismatch=ospfCntMaskMismatch, ospfIpRouteInst=ospfIpRouteInst, ospfIpRouteNextHop=ospfIpRouteNextHop, ospfIpRouteChassis=ospfIpRouteChassis, ospfCntBadVer=ospfCntBadVer, ospfCntNSSAOptMismatch=ospfCntNSSAOptMismatch, ospfCntNBMANeighbor=ospfCntNBMANeighbor, ospfIpRouteIfIndex=ospfIpRouteIfIndex, ospfCntOwnAddr=ospfCntOwnAddr, ospfIfCntEntry=ospfIfCntEntry, ospfCntChassis=ospfCntChassis, ospfIpRouteDest=ospfIpRouteDest, ospfCntMulticastVL=ospfCntMulticastVL, ospfCntExtOptMismatch=ospfCntExtOptMismatch, ospfIpRouteCost=ospfIpRouteCost, ospfIpRoutePref=ospfIpRoutePref, ospfCntAuthFail=ospfCntAuthFail, ospfIpRouteEntry=ospfIpRouteEntry, ospfIpRouteTable=ospfIpRouteTable, ospfCntTooShort=ospfCntTooShort, ospfCntBadType=ospfCntBadType, ospfCntLSAckTx=ospfCntLSAckTx, ospfCntLSUpdateRx=ospfCntLSUpdateRx, ospfCntBadLen=ospfCntBadLen, ospfCntDestAddr=ospfCntDestAddr, ospfCntLSUpdateTx=ospfCntLSUpdateTx, ospfCntBadAreaId=ospfCntBadAreaId, ospf=ospf)
