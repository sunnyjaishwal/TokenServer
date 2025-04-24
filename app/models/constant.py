
import random
class Mapping:
    '''
    Mapping class to hold the mapping of p_token and xd_token.
    Each mapping is represented as a list of two strings.
    '''
    p_token_1 = ['p_token_1', 'xd_token_1']
    p_token_2 = ['p_token_2', 'xd_token_2']
    p_token_3 = ['p_token_3', 'xd_token_3']
    p_token_4 = ['p_token_4', 'xd_token_4']
    p_token_5 = ['p_token_5', 'xd_token_5']
    p_token_6 = ['p_token_6', 'xd_token_6']
    p_token_7 = ['p_token_7', 'xd_token_7']
    p_token_8 = ['p_token_8', 'xd_token_8']
    p_token_9 = ['p_token_9', 'xd_token_9']
    p_token_10 = ['p_token_10', 'xd_token_10']
    p_token_11 = ['p_token_11', 'xd_token_11']
    p_token_12 = ['p_token_12', 'xd_token_12']
    p_token_13 = ['p_token_13', 'xd_token_13']
    p_token_14 = ['p_token_14', 'xd_token_14']
    p_token_15 = ['p_token_15', 'xd_token_15']
    p_token_16 = ['p_token_16', 'xd_token_16']
    p_token_17 = ['p_token_17', 'xd_token_17']
    p_token_18 = ['p_token_18', 'xd_token_18']
    p_token_19 = ['p_token_19', 'xd_token_19']
    p_token_20 = ['p_token_20', 'xd_token_20']
    p_token_21 = ['p_token_21', 'xd_token_21']
    p_token_22 = ['p_token_22', 'xd_token_22']
    p_token_23 = ['p_token_23', 'xd_token_23']
    p_token_24 = ['p_token_24', 'xd_token_24']
    p_token_25 = ['p_token_25', 'xd_token_25']
    p_token_26 = ['p_token_26', 'xd_token_26']
    p_token_27 = ['p_token_27', 'xd_token_27']
    p_token_28 = ['p_token_28', 'xd_token_28']
    p_token_29 = ['p_token_29', 'xd_token_29']
    p_token_30 = ['p_token_30', 'xd_token_30']
    p_token_31 = ['p_token_31', 'xd_token_31']
    p_token_32 = ['p_token_32', 'xd_token_32']
    p_token_33 = ['p_token_33', 'xd_token_33']
    p_token_34 = ['p_token_34', 'xd_token_34']
    p_token_35 = ['p_token_35', 'xd_token_35']
    p_token_36 = ['p_token_36', 'xd_token_36']
    p_token_37 = ['p_token_37', 'xd_token_37']
    p_token_38 = ['p_token_38', 'xd_token_38']
    p_token_39 = ['p_token_39', 'xd_token_39']
    p_token_40 = ['p_token_40', 'xd_token_40']
    p_token_41 = ['p_token_41', 'xd_token_41']
    p_token_42 = ['p_token_42', 'xd_token_42']
    p_token_43 = ['p_token_43', 'xd_token_43']
    p_token_44 = ['p_token_44', 'xd_token_44']
    p_token_45 = ['p_token_45', 'xd_token_45']
    p_token_46 = ['p_token_46', 'xd_token_46']
    p_token_47 = ['p_token_47', 'xd_token_47']
    p_token_48 = ['p_token_48', 'xd_token_48']
    p_token_49 = ['p_token_49', 'xd_token_49']
    p_token_50 = ['p_token_50', 'xd_token_50']

if __name__ == '__main__':
    # Example usage of the Mapping class
    # print(Mapping.p_token_1)  # Output: ['p_token_1', 'xd_token_1']
    # print(Mapping.p_token_2)  # Output: ['p_token_2', 'xd_token_2']
    # Add more examples as needed
    number = random.randint(1, 51)
    p_token, xd_token = getattr(Mapping, f'p_token_{number}')
    print(p_token, xd_token)  # Output: ['p_token_1', 'xd_token_1']
