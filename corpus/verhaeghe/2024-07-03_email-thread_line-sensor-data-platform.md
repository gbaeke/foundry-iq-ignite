# Email Thread: Firewall Request for the Line 1 Gateway

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-07-03 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Document type** | Email thread (exported) |

---

**From:** Jonas Peeters
**To:** Tine Desmet
**Cc:** Sofie Claes
**Date:** 2024-07-01 10:12
**Subject:** Line 1 gateway – status of the firewall request

Hi Tine,

The gateway for line 1 is mounted in the electrical cabinet and reads all 235 tags from the PLC. It buffers locally for now. As soon as outbound traffic to Azure IoT Hub is allowed, it can start sending.

Do you know where the firewall request stands? For the pilot milestone at the end of July we would need the rule in place by mid-July at the latest.

Thanks,
Jonas

---

**From:** Tine Desmet
**To:** Jonas Peeters
**Cc:** Sofie Claes
**Date:** 2024-07-02 16:47
**Subject:** RE: Line 1 gateway – status of the firewall request

Hi Jonas,

I submitted the wijzigingsaanvraag on 2024-06-20. It needs approval from our internal change board, which meets every two weeks, and then the external firewall partner has to implement it. The board looked at it yesterday and asked two questions:

1. Can the gateway be reached from the IT side or from the internet? (They want outbound only.)
2. Which exact destinations does it talk to? "Azure" is too broad for them.

Also, our firewall partner closes for the bouwverlof from 2024-07-15 for three weeks, with only an emergency line. If the change is not implemented before that, it will be August.

Tine

---

**From:** Jonas Peeters
**To:** Tine Desmet
**Cc:** Sofie Claes
**Date:** 2024-07-03 09:05
**Subject:** RE: Line 1 gateway – status of the firewall request

Hi Tine,

Answers for the change board:

1. Outbound only. The gateway opens the connection itself over TLS on port 443 (MQTT over WebSockets). Nothing needs to be opened inbound, not from IT and not from the internet.
2. Destination: the host name of Verhaeghe's IoT Hub, nothing else. I have put it in the attached sheet, with the IP ranges as fallback if the partner cannot filter on host names.

Each gateway has its own device identity in IoT Hub, so if one gateway is ever compromised we can disable it without touching the others.

Could you ask the board for an approval by e-mail instead of waiting for the next meeting? If the partner can do it before the 15th, we keep the end-of-July target.

Jonas

---

**From:** Sofie Claes
**To:** Tine Desmet, Jonas Peeters
**Cc:** Dries Callens
**Date:** 2024-07-03 11:30
**Subject:** RE: Line 1 gateway – status of the firewall request

Thanks both. Dries, for your information: the pilot line might start streaming later than end of July if the change misses the window before the bouwverlof. In the meantime we will build the lakehouse on manual exports from the line 1 HMI, so the team keeps moving. I will include this in the status report of 19 July.

Sofie
