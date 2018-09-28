
from lxml import etree
from ncclient import manager

if __name__ == "__main__":

    with manager.connect(host='192.168.10.80', port=830, username='admin', password='cisco',
                         hostkey_verify=False, device_params={'name': 'csr'},
                         allow_agent=False, look_for_keys=False) as device:

        nc_filter = """
                <config>
                <native xmlns="http://cisco.com/ns/yang/ned/ios">
                 <interface>
                  <Loopback>
                   <name>700</name>
                   <ip>
                    <address>
                        <primary>
                            <address>10.200.20.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                        <secondary>
                            <address>9.9.9.9</address>
                            <mask>255.255.255.0</mask>
                            <secondary/>
                        </secondary>
                    </address>
                   </ip>
                  </Loopback>
                 </interface>
                </native>
                </config>
        """

        nc_reply = device.edit_config(target='running', config=nc_filter)

        get_filter = """
            <native xmlns="http://cisco.com/ns/yang/ned/ios">
                INSERT CORRECT
                FILTER HERE
            </native>
        """

        # UNCOMMENT THE NEXT TWO LINES FOR THE LAB AFTER YOU
        # GET THE NEW SECONDARY IP WORKING
        nc_get_reply = device.get(('subtree', get_filter))
        print etree.tostring(nc_get_reply.data_ele, pretty_print=True)
